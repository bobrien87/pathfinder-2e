---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Healing]]"]
price: "{'gp': 20}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:3` (manipulate)

Healing vapor is a substance that accelerates natural recovery processes by dispersing a mist infused with a variety of reagents typically used for healing and recovery. When deployed from a sealed container, the vapors fill a @Template[burst|distance:5], last for 10 minutes, and can affect up to four living creatures at one time. Any creatures beyond the first four gain no benefit, though if a creature leaves before the duration is over, a new creature that enters can benefit from the mist. A creature benefiting from the vapors regains 1 Hit Point every 2 minutes. While affected, a creature also gains a +1 item bonus to saving throws against diseases and poisons. If the areas of more than one healing vapor overlap, only the strongest applies to creatures inside overlapping areas. Strong wind disperses the mist, rendering it ineffective while the wind blows.

**Source:** `= this.source` (`= this.source-type`)
