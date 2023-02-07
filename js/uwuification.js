const WORD_REPLACE = {
    "small": "smol",
    "cute": "kawaii~",
    "fluff": "floof",
    "love": "luv",
    "stupid": "baka",
    "idiot": "baka",
    "what": "nani",
    "meow": "nya~",
    "roar": "rawrr~",
}
// An object to match certain words for replacement words

const EMOJIS = [
    "rawr x3",
    "OwO",
    "UwU",
    "o.O",
    "-.-",
    ">w<",
    "(⑅˘꒳˘)",
    "(ꈍᴗꈍ)",
    "(˘ω˘)",
    "(U ᵕ U❁)",
    "σωσ",
    "òωó",
    "(///ˬ///✿)",
    "(U ﹏ U)",
    "( ͡o ω ͡o )",
    "ʘwʘ",
    ":3",
    ":3",  // important enough to have twice
    "XD",
    "nyaa~~",
    "mya",
    ">_<",
    "😳",
    "🥺",
    "😳😳😳",
    "rawr",
    "^^",
    "^^;;",
    "(ˆ ﻌ ˆ)♡",
    "^•ﻌ•^",
    "/(^•ω•^)",
    "(✿oωo)",
]
// A list of emojis/emoticons to add

function random_dice(strength) {
    return function() {
        return Math.random() < strength
    }
}

function randarr(arr) {
    return arr[Math.floor(Math.random() * arr.length)]
}

function reg(str, regex) {
    str = str.split(regex)
    for (let i = 0; i < str.length; i++) {
        temp = str[i]
        str[i] = temp.concat( ` ${randarr(EMOJIS)}`)
    }
    return str.join('')
}

function uwuify(
    text,
    stutter = random_dice(0.2),
    emojis = random_dice(0.1),
    tildes = random_dice(0.1),
) {
    text = text.toLowerCase()
    const keys = Object.keys(WORD_REPLACE)
    const values = Object.values(WORD_REPLACE)

    for (let i = 0; i < keys.length; i++) {
        text = text.replace(keys[i], values[i])
    }

    const patterns = [
        [String.raw`n([aeou][^aeiou])`, String.raw`ny\1`],
        [String.raw`(?<!w)[lr](?!w)`, "w"],
    ]

    text = reg(text, /[.!?\n]/gm)

    patterns.push([/(\s)([a-zA-Z])/gm, function(_) { if (stutter()) { return `$1$2-$2` } else { return `$1$2` } }])
    patterns.push([/\b(?=\s|$)/gm, function(_) { if (tildes()) { return `~` } else { return `` } }])

    for (var i = 0; i < patterns.length; i++) {
        subst = patterns[i][1]
        if (i > 1) subst = subst()
        text = text.replace(patterns[i][0], subst)
    }

    return text
}
