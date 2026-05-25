---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Bulwark]]", "[[Entrench melee]]", "[[Hindering]]"]
price: "{'gp': 1750}"
bulk: "5"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Worn by Iomedae's prestigious knights, this *+2 resilient bastion plate* is emblazoned with the Inheritor's religious symbol and sports a white cloak. While the cloak is white, this armor grants you a +2 item bonus to Diplomacy checks to [[Make an Impression]], provided your target has no enmity toward Iomedae.

**Activate** `pf2:1` (concentrate)

**Effect** The armor's cloak becomes red for 1 minute. As long as the cloak is red, you gain the benefits of the armor's deflect melee trait without needing to spend an additional action to activate it during each turn.

**Craft Requirements** You worship Iomedae.

**Source:** `= this.source` (`= this.source-type`)
