---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Clockwork]]"]
price: "{'gp': 10}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Powered by electricity, you can turn a mechanical torch on and off by toggling a lever on the torch with an Interact action. When active, the torch sheds bright light in either a 20-foot radius (and dim light to the next 40 feet) or a 40-foot cone (and dim light to the next 40 feet). Changing this area requires a single Interact action to flip a switch. The torch carries sufficient charge to operate for ten minutes. You can recharge the torch in 1 minute via an integrated crank-charging mechanism, turning the clockwork gears and generating sparks to power the torch, though doing so requires two hands.

**Source:** `= this.source` (`= this.source-type`)
