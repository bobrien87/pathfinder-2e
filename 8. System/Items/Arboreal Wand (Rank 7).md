---
type: item
source-type: "Remaster"
level: "19"
traits: ["[[Healing]]", "[[Magical]]", "[[Vitality]]", "[[Wand]]"]
price: "{'gp': 40000}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder #201: Pactbreaker"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This gnarled wand is made from the branch of an arboreal.

**Activate** Cast a Spell

**Frequency** once per day, plus overcharge

**Effect** You cast [[Heal]] at the indicated rank. After you cast the spell, the raw primal energy stored within the arboreal from which the wand was made washes over one target you choose and tries to purify its essence. The wand attempts to counteract the lowest level affliction affecting your target. It uses your casting modifier and a counteract rank of half the wand's item level rounded up.

**Craft Requirements** Supply a casting of *heal* of the appropriate rank and a branch freely given by an arboreal.

**Source:** `= this.source` (`= this.source-type`)
