---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Cold]]", "[[Grimoire]]", "[[Primal]]"]
price: "{'gp': 430}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The first 12 pages of this tome tell the same story in two languages: 6 pages in Skald and 6 pages in the ancient Jotun dialect used by saumen kar, a species of ice-dwelling humanoids. The story is a tale of a saumen kar stricken with snow blindness after spending too long under the sun building snow giants.

**Activate** `pf2:f` (concentrate)

**Frequency** once per day

**Effect** If your next action is to cast a cold spell that deals damage, all creatures damaged by the spell are also [[Dazzled]] for 3 rounds by light refracting and reflecting within and around the spell's chilling effects. If an affected creature critically failed its save against the required spell, or if you critically succeeded on your spell attack roll against the creature, it's instead [[Blinded]] for 1 round and then dazzled for 3 rounds.

**Source:** `= this.source` (`= this.source-type`)
