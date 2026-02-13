<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Démonstration Birthday Attack - Mini-projet 6</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }

        .container {
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            padding: 40px;
            max-width: 900px;
            width: 100%;
        }

        h1 {
            color: #2E5090;
            text-align: center;
            margin-bottom: 10px;
            font-size: 2em;
        }

        .subtitle {
            text-align: center;
            color: #666;
            margin-bottom: 30px;
            font-size: 0.95em;
        }

        .tabs {
            display: flex;
            gap: 10px;
            margin-bottom: 30px;
            border-bottom: 2px solid #eee;
        }

        .tab {
            padding: 12px 24px;
            background: none;
            border: none;
            cursor: pointer;
            font-size: 16px;
            color: #666;
            border-bottom: 3px solid transparent;
            transition: all 0.3s;
        }

        .tab:hover {
            color: #2E5090;
        }

        .tab.active {
            color: #2E5090;
            border-bottom-color: #2E5090;
            font-weight: bold;
        }

        .tab-content {
            display: none;
        }

        .tab-content.active {
            display: block;
            animation: fadeIn 0.3s;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Login Section */
        .login-box {
            max-width: 400px;
            margin: 0 auto;
        }

        .form-group {
            margin-bottom: 20px;
        }

        label {
            display: block;
            margin-bottom: 8px;
            color: #333;
            font-weight: 500;
        }

        input[type="text"],
        input[type="password"],
        select {
            width: 100%;
            padding: 12px;
            border: 2px solid #ddd;
            border-radius: 8px;
            font-size: 14px;
            transition: border-color 0.3s;
        }

        input:focus, select:focus {
            outline: none;
            border-color: #667eea;
        }

        .btn {
            width: 100%;
            padding: 14px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            transition: transform 0.2s, box-shadow 0.2s;
        }

        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        }

        .btn:active {
            transform: translateY(0);
        }

        .btn-secondary {
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            margin-top: 10px;
        }

        .hash-display {
            margin-top: 20px;
            padding: 15px;
            background: #f5f5f5;
            border-radius: 8px;
            border-left: 4px solid #2E5090;
        }

        .hash-label {
            font-weight: bold;
            color: #2E5090;
            margin-bottom: 5px;
        }

        .hash-value {
            font-family: 'Courier New', monospace;
            color: #333;
            word-break: break-all;
            font-size: 13px;
        }

        /* Simulation Section */
        .controls {
            display: flex;
            gap: 15px;
            margin-bottom: 25px;
            flex-wrap: wrap;
        }

        .control-group {
            flex: 1;
            min-width: 200px;
        }

        .results-box {
            background: #f9f9f9;
            border-radius: 12px;
            padding: 25px;
            margin-top: 20px;
        }

        .stat-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin-bottom: 20px;
        }

        .stat-card {
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
            text-align: center;
        }

        .stat-value {
            font-size: 2em;
            font-weight: bold;
            color: #2E5090;
            margin-bottom: 5px;
        }

        .stat-label {
            color: #666;
            font-size: 0.9em;
        }

        .collision-display {
            background: white;
            padding: 20px;
            border-radius: 10px;
            margin-top: 15px;
            border: 2px solid #4CAF50;
        }

        .collision-title {
            color: #4CAF50;
            font-weight: bold;
            font-size: 1.2em;
            margin-bottom: 15px;
            text-align: center;
        }

        .message-box {
            background: #f5f5f5;
            padding: 12px;
            border-radius: 6px;
            margin-bottom: 10px;
            font-family: 'Courier New', monospace;
            font-size: 12px;
            word-break: break-all;
        }

        .progress-bar {
            width: 100%;
            height: 8px;
            background: #eee;
            border-radius: 4px;
            overflow: hidden;
            margin: 15px 0;
        }

        .progress-fill {
            height: 100%;
            background: linear-gradient(90deg, #667eea, #764ba2);
            transition: width 0.3s;
            animation: pulse 1.5s infinite;
        }

        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.7; }
        }

        .info-box {
            background: #e3f2fd;
            border-left: 4px solid #2196F3;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 20px;
        }

        .info-box h3 {
            color: #1976D2;
            margin-bottom: 10px;
        }

        .warning-box {
            background: #fff3cd;
            border-left: 4px solid #ffc107;
            padding: 15px;
            border-radius: 8px;
            margin-top: 20px;
        }

        .success-box {
            background: #d4edda;
            border-left: 4px solid #28a745;
            padding: 15px;
            border-radius: 8px;
            margin-top: 20px;
        }

        /* Theory Section */
        .theory-content {
            line-height: 1.8;
        }

        .theory-content h2 {
            color: #2E5090;
            margin-top: 25px;
            margin-bottom: 15px;
        }

        .theory-content h3 {
            color: #667eea;
            margin-top: 20px;
            margin-bottom: 10px;
        }

        .formula {
            background: #f5f5f5;
            padding: 15px;
            border-radius: 8px;
            text-align: center;
            font-family: 'Courier New', monospace;
            font-size: 1.2em;
            margin: 15px 0;
            border: 2px solid #ddd;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }

        th, td {
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }

        th {
            background: #2E5090;
            color: white;
            font-weight: bold;
        }

        tr:hover {
            background: #f5f5f5;
        }

        .hidden {
            display: none;
        }

        @media (max-width: 768px) {
            .container {
                padding: 20px;
            }

            h1 {
                font-size: 1.5em;
            }

            .controls {
                flex-direction: column;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🔐 Démonstration Birthday Attack</h1>
        <p class="subtitle">Mini-projet 6 - Étude des faiblesses cryptographiques</p>

        <div class="tabs">
            <button class="tab active" onclick="switchTab('login')">🔑 Connexion</button>
            <button class="tab" onclick="switchTab('simulation')">⚡ Simulation</button>
            <button class="tab" onclick="switchTab('theory')">📚 Théorie</button>
        </div>

        <!-- TAB 1: LOGIN -->
        <div id="login-tab" class="tab-content active">
            <div class="login-box">
                <div class="info-box">
                    <h3>🎯 Testez la vulnérabilité</h3>
                    <p>Cette page simule un système de connexion utilisant différents algorithmes de hachage. Voyez comment la taille du hash affecte la sécurité.</p>
                </div>

                <form id="login-form">
                    <div class="form-group">
                        <label for="username">👤 Nom d'utilisateur</label>
                        <input type="text" id="username" placeholder="Entrez votre nom" required>
                    </div>

                    <div class="form-group">
                        <label for="password">🔒 Mot de passe</label>
                        <input type="password" id="password" placeholder="Entrez votre mot de passe" required>
                    </div>

                    <div class="form-group">
                        <label for="hash-algo">⚙️ Algorithme de hachage</label>
                        <select id="hash-algo">
                            <option value="16">Faible (16 bits) - VULNÉRABLE</option>
                            <option value="32">Moyen (32 bits) - Peu sûr</option>
                            <option value="64">MD5 simulé (64 bits) - Déconseillé</option>
                            <option value="128">SHA-256 simulé (128 bits) - Sécurisé</option>
                        </select>
                    </div>

                    <button type="submit" class="btn">Se connecter</button>
                </form>

                <div id="login-result" class="hidden"></div>
            </div>
        </div>

        <!-- TAB 2: SIMULATION -->
        <div id="simulation-tab" class="tab-content">
            <div class="info-box">
                <h3>⚡ Simulation d'attaque en temps réel</h3>
                <p>Observez combien de tentatives sont nécessaires pour trouver une collision selon la taille du hash.</p>
            </div>

            <div class="controls">
                <div class="control-group">
                    <label for="sim-bits">Taille du hash (bits)</label>
                    <select id="sim-bits">
                        <option value="12">12 bits (~4,096 valeurs)</option>
                        <option value="16" selected>16 bits (~65,536 valeurs)</option>
                        <option value="20">20 bits (~1 million valeurs)</option>
                        <option value="24">24 bits (~16 millions valeurs)</option>
                    </select>
                </div>

                <div class="control-group">
                    <label for="sim-speed">Vitesse de simulation</label>
                    <select id="sim-speed">
                        <option value="1">Lente (1 ms/essai)</option>
                        <option value="0.1" selected>Normale (0.1 ms/essai)</option>
                        <option value="0.01">Rapide (0.01 ms/essai)</option>
                    </select>
                </div>
            </div>

            <button class="btn" onclick="startSimulation()">🚀 Lancer la simulation</button>
            <button class="btn btn-secondary" onclick="stopSimulation()">⏹️ Arrêter</button>

            <div id="simulation-results" class="hidden">
                <div class="results-box">
                    <div class="stat-grid">
                        <div class="stat-card">
                            <div class="stat-value" id="attempts-count">0</div>
                            <div class="stat-label">Tentatives</div>
                        </div>
                        <div class="stat-card">
                            <div class="stat-value" id="theoretical-value">0</div>
                            <div class="stat-label">Valeur théorique</div>
                        </div>
                        <div class="stat-card">
                            <div class="stat-value" id="elapsed-time">0s</div>
                            <div class="stat-label">Temps écoulé</div>
                        </div>
                        <div class="stat-card">
                            <div class="stat-value" id="hash-rate">0</div>
                            <div class="stat-label">Hash/seconde</div>
                        </div>
                    </div>

                    <div class="progress-bar">
                        <div class="progress-fill" id="progress-bar" style="width: 0%"></div>
                    </div>

                    <div id="collision-result" class="hidden"></div>
                </div>
            </div>
        </div>

        <!-- TAB 3: THEORY -->
        <div id="theory-tab" class="tab-content">
            <div class="theory-content">
                <h2>📖 Le paradoxe des anniversaires</h2>
                <p>Dans un groupe de seulement 23 personnes, il y a plus de 50% de chance que deux personnes partagent le même anniversaire. Ce résultat contre-intuitif s'applique aux fonctions de hachage.</p>

                <h3>Formule mathématique</h3>
                <div class="formula">
                    n ≈ √(2N × ln(1/(1-p)))
                </div>
                <p><strong>où :</strong> n = nombre d'essais, N = espace de possibilités, p = probabilité</p>

                <h3>Application en cryptographie</h3>
                <div class="formula">
                    Complexité = 2^(n/2) au lieu de 2^n
                </div>

                <h3>Tableau comparatif</h3>
                <table>
                    <thead>
                        <tr>
                            <th>Algorithme</th>
                            <th>Taille</th>
                            <th>Force brute</th>
                            <th>Birthday Attack</th>
                            <th>Sécurité</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>MD5</td>
                            <td>128 bits</td>
                            <td>2^128</td>
                            <td>2^64</td>
                            <td>❌ Vulnérable</td>
                        </tr>
                        <tr>
                            <td>SHA-1</td>
                            <td>160 bits</td>
                            <td>2^160</td>
                            <td>2^80</td>
                            <td>⚠️ Déconseillé</td>
                        </tr>
                        <tr>
                            <td>SHA-256</td>
                            <td>256 bits</td>
                            <td>2^256</td>
                            <td>2^128</td>
                            <td>✅ Sécurisé</td>
                        </tr>
                        <tr>
                            <td>SHA-512</td>
                            <td>512 bits</td>
                            <td>2^512</td>
                            <td>2^256</td>
                            <td>✅ Très sécurisé</td>
                        </tr>
                    </tbody>
                </table>

                <div class="warning-box">
                    <strong>⚠️ Conclusion importante :</strong> Une fonction de hachage de n bits offre seulement n/2 bits de sécurité contre les attaques par collision. C'est pourquoi MD5 (64 bits de sécurité réelle) et SHA-1 (80 bits) sont obsolètes.
                </div>
            </div>
        </div>
    </div>

    <script>
        let simulationRunning = false;
        let simulationInterval = null;
        let startTime = null;

        // Tab switching
        function switchTab(tabName) {
            document.querySelectorAll('.tab').forEach(tab => tab.classList.remove('active'));
            document.querySelectorAll('.tab-content').forEach(content => content.classList.remove('active'));
            
            event.target.classList.add('active');
            document.getElementById(tabName + '-tab').classList.add('active');
        }

        // Simple hash function (for demonstration only)
        async function simpleHash(text, bits) {
            const encoder = new TextEncoder();
            const data = encoder.encode(text);
            const hashBuffer = await crypto.subtle.digest('SHA-256', data);
            const hashArray = Array.from(new Uint8Array(hashBuffer));
            const hashHex = hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
            
            // Truncate to specified bits
            const maxValue = Math.pow(2, bits);
            const truncated = parseInt(hashHex.substring(0, 16), 16) % maxValue;
            
            return {
                full: hashHex,
                truncated: truncated,
                hex: truncated.toString(16).padStart(Math.ceil(bits/4), '0')
            };
        }

        // Login form handler
        document.getElementById('login-form').addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;
            const bits = parseInt(document.getElementById('hash-algo').value);
            
            const hash = await simpleHash(username + password, bits);
            
            const resultDiv = document.getElementById('login-result');
            resultDiv.className = 'hash-display';
            resultDiv.innerHTML = `
                <div class="hash-label">✅ Connexion réussie !</div>
                <div class="hash-label" style="margin-top: 15px;">Hash généré (${bits} bits) :</div>
                <div class="hash-value">${hash.hex}</div>
                <div class="hash-label" style="margin-top: 15px;">Hash complet SHA-256 :</div>
                <div class="hash-value">${hash.full}</div>
                ${bits <= 64 ? '<div class="warning-box" style="margin-top: 15px;"><strong>⚠️ Attention :</strong> Cet algorithme est vulnérable aux attaques Birthday. Un attaquant pourrait trouver une collision en ~' + Math.pow(2, bits/2).toLocaleString() + ' tentatives.</div>' : ''}
                ${bits >= 128 ? '<div class="success-box" style="margin-top: 15px;"><strong>✅ Sécurisé :</strong> Cet algorithme offre une protection adéquate contre les attaques Birthday (~2^' + (bits/2) + ' tentatives nécessaires).</div>' : ''}
            `;
        });

        // Birthday attack simulation
        async function startSimulation() {
            if (simulationRunning) return;
            
            simulationRunning = true;
            const bits = parseInt(document.getElementById('sim-bits').value);
            const speed = parseFloat(document.getElementById('sim-speed').value);
            const maxHash = Math.pow(2, bits);
            const theoretical = Math.sqrt(Math.PI * maxHash / 2);
            
            document.getElementById('simulation-results').classList.remove('hidden');
            document.getElementById('theoretical-value').textContent = Math.round(theoretical).toLocaleString();
            document.getElementById('collision-result').classList.add('hidden');
            
            const seenHashes = new Map();
            let attempts = 0;
            startTime = Date.now();
            
            const simulate = async () => {
                if (!simulationRunning) return;
                
                attempts++;
                const message = 'msg_' + Math.random().toString(36).substring(2);
                const hash = await simpleHash(message, bits);
                
                // Update stats
                const elapsed = (Date.now() - startTime) / 1000;
                const rate = Math.round(attempts / elapsed);
                const progress = Math.min((attempts / theoretical) * 100, 100);
                
                document.getElementById('attempts-count').textContent = attempts.toLocaleString();
                document.getElementById('elapsed-time').textContent = elapsed.toFixed(2) + 's';
                document.getElementById('hash-rate').textContent = rate.toLocaleString();
                document.getElementById('progress-bar').style.width = progress + '%';
                
                // Check collision
                if (seenHashes.has(hash.truncated)) {
                    simulationRunning = false;
                    const collisionMsg = seenHashes.get(hash.truncated);
                    
                    document.getElementById('collision-result').innerHTML = `
                        <div class="collision-display">
                            <div class="collision-title">🎉 COLLISION TROUVÉE !</div>
                            <div class="hash-label">Message 1 :</div>
                            <div class="message-box">${collisionMsg}</div>
                            <div class="hash-label">Message 2 :</div>
                            <div class="message-box">${message}</div>
                            <div class="hash-label">Hash en collision (${bits} bits) :</div>
                            <div class="message-box" style="color: #4CAF50; font-weight: bold;">${hash.hex}</div>
                            <div class="success-box" style="margin-top: 15px;">
                                <strong>Résultat :</strong> Collision trouvée en ${attempts.toLocaleString()} tentatives 
                                (théorique: ${Math.round(theoretical).toLocaleString()}, 
                                écart: ${(((attempts - theoretical) / theoretical) * 100).toFixed(1)}%)
                            </div>
                        </div>
                    `;
                    document.getElementById('collision-result').classList.remove('hidden');
                    return;
                }
                
                seenHashes.set(hash.truncated, message);
                
                // Continue simulation
                setTimeout(simulate, speed);
            };
            
            simulate();
        }

        function stopSimulation() {
            simulationRunning = false;
        }
    </script>
</body>
</html>