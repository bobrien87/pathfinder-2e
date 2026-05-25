---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Grimoire]]", "[[Magical]]"]
price: "{'gp': 700}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This well-worn manuscript is side stitched with fading lilac-colored thread. It's filled with poems written long ago by a philosopher named Seiji Juubun, containing a lifetime of wisdom and presenting information and advice on a tremendous breadth of topics.

**Activate—Poetic Spellcasting** `pf2:1` (concentrate, emotion, mental, spellshape)

**Frequency** once per day

**Effect** If your next action is to Cast a Spell that has the linguistic trait and that targets 1 creature, you're overtaken by Juubun's spirit, and the spoken elements of your spell become impressively poetic. If the target is an ally, your words inspire them and they gain 10 temporary Hit Points that last for 1 minute. If the targeted creature is an enemy and the spell requires a saving throw, and if the enemy fails its saving throw, they become [[Sickened]] 1 as a result of despair and sadness.

> [!danger] Effect: Juubun's One Thousand Poems

**Source:** `= this.source` (`= this.source-type`)
