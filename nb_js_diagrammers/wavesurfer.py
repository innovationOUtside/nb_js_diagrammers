TEMPLATE_WAVESURFERJS = """<html>
    <body>
        <script src="https://unpkg.com/wavesurfer.js/dist/wavesurfer.js"></script>
        <div id="wavesurfer">
            <div id="waveform"></div>
            <div class="controls">
                <button class="btn btn-primary" data-action="play">
                    <i class="glyphicon glyphicon-play"></i>
                    Play
                    /
                    <i class="glyphicon glyphicon-pause"></i>
                    Pause
                </button>
            </div>
        </div>
        <script>
            var GLOBAL_ACTIONS = {{ // eslint-disable-line
                play: function() {{
                    window.wavesurfer.playPause();
                }},
 
                back: function() {{
                    window.wavesurfer.skipBackward();
                }},
 
                forth: function() {{
                    window.wavesurfer.skipForward();
                }},
 
                'toggle-mute': function() {{
                    window.wavesurfer.toggleMute();
                }}
            }};
 
            // Bind actions to buttons and keypresses
            document.addEventListener('DOMContentLoaded', function() {{
                document.addEventListener('keydown', function(e) {{
                    let map = {{
                        32: 'play', // space
                        37: 'back', // left
                        39: 'forth' // right
                    }};
                    let action = map[e.keyCode];
                    if (action in GLOBAL_ACTIONS) {{
                        if (document == e.target || document.body == e.target || e.target.attributes["data-action"]) {{
                            e.preventDefault();
                        }}
                        GLOBAL_ACTIONS[action](e);
                    }}
                }});
 
                [].forEach.call(document.querySelectorAll('[data-action]'), function(el) {{
                    el.addEventListener('click', function(e) {{
                        let action = e.currentTarget.dataset.action;
                        if (action in GLOBAL_ACTIONS) {{
                            e.preventDefault();
                            GLOBAL_ACTIONS[action](e);
                        }}
                    }});
                }});
            }});
        </script>
 
        <script>
            var wavesurfer = WaveSurfer.create({{
                container: '#waveform',
                waveColor: 'violet',
                backend: 'MediaElement',
                progressColor: 'purple'
            }});
        </script>
        <script>
            wavesurfer.load("{src}");
        </script>
    </body>
</html>
"""