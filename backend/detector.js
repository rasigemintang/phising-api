const phishingKeywords = ['login', 'free', 'verify', 'update', 'bank', 'secure', 'account', 'paypal'];

function detectPhishing(url) {
    return phishingKeywords.some(keyword => url.toLowerCase().includes(keyword));
}

module.exports = { detectPhishing };
