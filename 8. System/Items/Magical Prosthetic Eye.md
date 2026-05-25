---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Magical]]"]
price: "{'gp': 5}"
usage: "worn"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This prosthetic eye converts visible light into a telepathic signal that is relayed to the wearer's mind using magic. As the wearer's mind must process the telepathic signal in the same way as it would a nerve impulse, the acuity and other abilities related to the vision provided by the magical prosthetic eye matches that of other members of your ancestry (for instance, a goblin with a magical prosthetic eye would be able to see in darkvision, while a human wearing the same prosthetic would need illumination). You can remove or replace a magical prosthetic eye using an Interact action.

**Source:** `= this.source` (`= this.source-type`)
