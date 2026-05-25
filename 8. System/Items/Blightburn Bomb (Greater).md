---
type: item
source-type: "Remaster"
level: "20"
traits: ["[[Alchemical]]", "[[Bomb]]", "[[Consumable]]", "[[Disease]]", "[[Poison]]", "[[Splash]]"]
price: "{'gp': 12000}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` Strike

Blightburn bombs have radioactive materials sealed inside flasks treated with lead. The bomb grants a +3 item bonus to attack rolls and deals 4d6 poison damage, 4d4 persistent poison damage, and 4 poison splash damage. A creature that takes the persistent poison damage deals the splash damage again from its current position as the radiation continues to harm nearby creatures. The persistent damage can last up to 1 minute. Blightburn bombs also expose the primary target to blightburn sickness.

**Saving Throw** DC 43 [[Fortitude]] save

**Onset** 1d4 days

**Stage 1** [[Drained]] 1 (1 day)

**Stage 2** drained 1 and [[Sickened]] 1 (1 day)

**Stage 3** [[Drained]] 2 and [[Sickened]] 2 (1 week)

**Stage 4** [[Drained]] 3 and [[Sickened]] 3 (1 month)

**Stage 5** increase drained condition by 1 (1 year)

**Source:** `= this.source` (`= this.source-type`)
