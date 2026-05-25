---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Coda]]", "[[Occult]]", "[[Staff]]"]
price: "{'gp': 4500}"
usage: "held-in-two-hands"
bulk: "1"
source: "Pathfinder #211: The Secret of Deathstalk Tower"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This 21-stringed instrument symbolizes connectivity with the past, present, and future. The kora grants a +2 item bonus to Performance checks made to tell stories when used to accompany song or speech.

The *kora of the unending story* is a coda instrument—an item that functions like a staff but in the form of a musical instrument.

**Activate** Cast a Spell

**Effect** You expend a number of charges from the kora to cast a spell from its list.

- **Cantrip** [[Read Aura]]
- **1st** [[Object Reading]]
- **2nd** [[Augury]]
- **3rd** [[Mind Reading]]
- **4th** [[Read Omens]]
- **5th** [[Vision of Death]]
- **6th** [[Object Reading]]

**Source:** `= this.source` (`= this.source-type`)
