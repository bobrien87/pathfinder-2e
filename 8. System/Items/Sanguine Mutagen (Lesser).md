---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Elixir]]", "[[Mutagen]]", "[[Polymorph]]"]
price: "{'gp': 3}"
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

For 1 minute you gain greatly increased blood production, filtering out contagions and boosting your endurance but causing your body to bloat with blood.

**Benefit** You gain a +1 item bonus to Fortitude and Reflex saves. This bonus improves to +2 when you attempt a save against an effect that has the disease trait, poison trait, or would give you the [[Fatigued]] condition.

**Drawback** Whenever you take piercing or slashing damage, you take 1d6 bleed.

> [!danger] Effect: Sanguine Mutagen (Lesser)

**Source:** `= this.source` (`= this.source-type`)
