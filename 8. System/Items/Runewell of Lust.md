---
type: item
source-type: "Remaster"
level: "23"
traits: ["[[Artifact]]", "[[Magical]]"]
price: "{'value': {}}"
usage: "other"
bulk: "L"
source: "Pathfinder #221: Into the Apocalypse Archive"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The Runewell of Lust is a potent artifact and was the first of its kind among the runelords. As with all runewells, the Runewell of Lust is immobile and located within a demiplane that's inexorably linked to it, but the anima focus that allows access to the demiplane and the runewell can be transported to new locations through a series of complex rites known only to Sorshen herself.

Originally, the Runewell of Lust could absorb soul fragments of those who served Sorshen upon their deaths, granting her an essentially limitless supply of magical power she could use to fund potent rituals or craft magical items, but she disabled this ability soon after she woke years ago and decided it was time for a change. The Runewell of Lust appears as a hot spring filled with soothing 3-foot-deep waters.

**Activate—Exit the Eye** `pf2:1` (concentrate, manipulate)

**Effect** By splashing the runewell's water on yourself while you stand within it, you transport yourself back to a space of your choice within 30 feet of the anima focus, which is currently located in Sorshen's atrium.

**Destruction** If Sorshen is slain, the waters within the Runewell of Lust immediately become normal water, destroying the runewell in the process. The Eye of Desire is destroyed as well. Creatures not native to the Eye of Desire are immediately transported to the vicinity of the runewell's linked anima focus and become [[Stunned]] 3; any foreign objects within the Eye of Desire at the time are similarly ejected.

**Source:** `= this.source` (`= this.source-type`)
