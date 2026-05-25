---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Consumable]]", "[[Magical]]", "[[Potion]]"]
price: "{'gp': 55}"
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

A foamy, cloudy liquid, hovering potion enables you to defy gravity for 5 minutes. By default, the potion causes you to float several inches off the ground. If you take a Stride action, you can move 10 feet up or down in the air. You can instead Climb at your full Speed or Stride to move along a horizontal surface at half your Speed. The GM determines which surfaces can be climbed or moved across this way. If you fall while this potion is in effect, you can use the Arrest a Fall reaction as if you had a fly Speed. If you have a fly Speed, you remain airborne at the end of your turn, even if you didn't use a Fly action this round.

**Source:** `= this.source` (`= this.source-type`)
