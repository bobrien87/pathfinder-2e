---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Elixir]]", "[[Healing]]"]
price: "{'gp': 160}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

First created using the same principles as the antiplague and antivenom elixirs, an affliction suppressant is a broadly useful medicine, but sacrifices potency. It applies to a wide variety of afflictions, but lasts a much shorter time. Upon drinking an affliction suppressant, you gain a +3 item bonus to all saves against afflictions for 10 minutes.

Unlike with an antiplague, this suppressant isn't long-lasting enough to apply to a daily save against the progression of a disease, curse, or other long-lasting affliction. It can still help protect you from catching such an affliction when you're initially exposed to it, as well as on saves that occur after stages that last 10 minutes or less.

**Source:** `= this.source` (`= this.source-type`)
