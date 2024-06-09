// src/components/GoogleAuth.js
import React from 'react';
function GoogleAuth() {
    return (
        <div>
            <a href="/core/auth/google/">Authenticate with Google</a>
        </div>
    );
}
export default GoogleAuth;
// src/components/MicrosoftAuth.js
import React from 'react';
function MicrosoftAuth() {
    return (
        <div>
            <a href="/core/auth/microsoft/">Authenticate with Microsoft</a>
        </div>
    );
}
export default MicrosoftAuth;
// src/components/MergedData.js
import React, { useState, useEffect } from 'react';
function MergedData() {
    const [data, setData] = useState(null);
    useEffect(() => {
        fetch('/core/merge/')
            .then(response => response.json())
            .then(data => setData(data));
    }, []);
    return (
        <div>
            {data ? (
                <pre>{JSON.stringify(data, null, 2)}</pre>
            ) : (
                <p>Loading...</p>
            )}
        </div>
    );
}
export default MergedData;