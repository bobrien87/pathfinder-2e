---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Magical]]", "[[Mental]]", "[[Sleep]]", "[[Wand]]"]
price: "{'cp': 0, 'gp': 1000, 'pp': 0, 'sp': 0}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The carved talon of an unidentifiable beast comprises this wand. Blood-stained cloth wraps the thicker part of the talon, which acts as a handle.

**Activate** Cast a Spell

**Frequency** once per day, plus overcharge

**Effect** You cast 4th-rank [[Sleep]], but the slumbering creatures have terrifying nightmares. A creature knocked [[Unconscious]] by this spell takes 1d6 persistent,mental. This damage wakes the creature from unconsciousness only if it deals 4 or more damage on a single roll. If the creature awakens from its unconsciousness due to damage (whether it was the persistent mental damage or not), it's [[Frightened]] 1. If it awakens from damage on its own turn, the creature doesn't reduce its frightened condition automatically on that turn.

**Craft Requirements** Supply a casting of 4th-rank *sleep*.

**Source:** `= this.source` (`= this.source-type`)
