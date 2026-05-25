---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Consumable]]", "[[Magical]]", "[[Oil]]"]
price: "{'gp': 150}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Adventure Path: Gatewalkers"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** 1 minute (Interact)

Adlet spiritual leaders create this thick purple gel so that the dead can temporarily assume their appearance in life during ancestral worship ceremonies. Spreading it over the bones of an undead creature or a lifeless corpse causes the gel to congeal, forming a cosmetic layer that covers or restores any missing or compromised flesh until the body mimics its appearance in life. The dead creature's flesh looks healthy and whole. It gains a +2 circumstance bonus on Deception checks to look like a living creature. The gel does not restore life or Hit Points and the flesh quickly rots away 8 hours after application.

> [!danger] Effect: Oil of Corpse Restoration

**Source:** `= this.source` (`= this.source-type`)
