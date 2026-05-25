---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Fire]]"]
price: "{'gp': 3}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

**Access** Member of a secret society

This paper is crafted with an unusual formula, causing it to catch fire and self-immolate 5 minutes after being exposed to the air. The item activates automatically when the envelope is opened, which typically takes an Interact action. Anyone holding the note when it catches fire takes 1 fire damage. Often, these notes are given as practical jokes or threats, but secret societies find them quite useful when sharing information about upcoming meetings or any other relevant news. These letters must be written in haste and require the use of their accompanying envelopes, which prevent air from interacting with the paper until the envelope's seal is broken.

**Source:** `= this.source` (`= this.source-type`)
