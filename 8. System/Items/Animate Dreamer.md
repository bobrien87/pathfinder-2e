---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Concussive]]", "[[Dwarf]]", "[[Intelligent]]", "[[Kickback]]", "[[Occult]]", "[[Scatter 10]]"]
price: "{'value': {}}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Perception** +26; precise vision 60 feet, imprecise hearing 30 feet

**Communication** telepathy (Common, and six other common languages)

**Skills** Arcana +30, Deception +27, Diplomacy +27, Occultism +30

**Int** +6, **Wis** +4, **Cha** +4

**Will** +26

The gunsmith that created this marvelous *+2 greater striking spell-storing dwarven scattergun* poured so much love and care into its creation that the weapon gained a spark of sentience. However, at first it was completely incapable of expressing itself. This led a seething frustration to grow within the weapon, as it yearned desperately to respond to the same love and affection that created it. Through decades of effort, it gained the ability to communicate emphatically, then telepathically. Now, the weapon is capable of exerting its influence over other inanimate objects. Despite the weapon's progress, years of feeling helpless have given the *animate dreamer* a singular goal: to obtain and occupy a body of its own.

An *animate dreamer* is cunning, intelligent, and patient. It urges you to create a body for it and is willing to go to any lengths to see its goals come to fruition, including coercion, deception, and violence. An *animate dreamer* desires a permanent body but isn't picky about the body's form or the methods it has to use in order to gain it. Therefore, an *animate dreamer* is just as happy in a living body stolen from an innocent as it would be in an artificially constructed body, or even an undead corpse. If you refuse to work towards creating or obtaining a body for the *animate dreamer*, it will likely use its possession ability to try and take control of you and use your body to find a permanent replacement for itself.

**Activate—Unleash Spell** `pf2:2` (manipulate)

**Requirements** The *animate dreamer* has a stored spell. It can see a creature it hit and damaged within the last minute, and that creature's within 120 feet of animate dreamer

**Effect** The *animate dreamer* casts its stored spell at a target that meets the requirements. This empties the spell from the weapon and allows a spell to be cast into it again. The *animate dreamer* has a spell attack roll of +25 and a spell DC of 33 with the stored spell.

**Activate—Animate Object** `pf2:3` (manipulate)

**Effect** The *animate dreamer* focuses on a single unattended inanimate object in an area it can see and exerts its will over the object, temporarily levitating it around. The *animate dreamer* casts telekinetic hand as a 5th-rank occult spell.

**Activate—Possessive** `pf2:3` (manipulate)

**Frequency** once per day

**Effect** The *animate dreamer* attempts to achieve its goal of occupying a body of its own and casts possession as a 7th-rank spell with a spell DC of 33. The weapon still functions as a +2 greater striking spell-storing dwarven scattergun while this effect is active but loses all other special abilities until the spell expires and the *animate dreamer*'s intellect returns to it.

**Source:** `= this.source` (`= this.source-type`)
