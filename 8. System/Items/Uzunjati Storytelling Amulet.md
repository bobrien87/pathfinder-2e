---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 145}"
usage: "worn"
bulk: "—"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This round, flat amulet can be made of metal, clay, or leather and is usually highly personalized with runes, sigils, lines of poetry, or a depiction of a storyteller at work. In Azimbye's case, their gold-rimmed metal amulet boasts fine dwarven workmanship, and bears lines from one of the oldest epic poems of the legendary folk hero Kgalaserke on one side and a stylized portrait of a storytelling event in Ranage's Circle on the other. While wearing the amulet, you gain a +1 item bonus to Performance checks.

**Activate—Enamoring Story** `pf2:f` (concentrate)

**Frequency** once per day

**Trigger** The perfect anecdote or story to impress your interlocutor comes floating to your memory.

You attempt to Make an Impression or Request, using a Performance check instead of a Diplomacy check.

**Source:** `= this.source` (`= this.source-type`)
