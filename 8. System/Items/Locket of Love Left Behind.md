---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 1200}"
usage: "worn"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

There's a tiny picture of a beloved partner, child, or even place nestled inside this small gold locket with a heart on the front. The locket reminds you that no matter how terrible the ravages of war are, you have something very important to live for. While wearing the necklace, you gain a +5-foot status bonus to your Speeds when you have the [[Fleeing]] condition. If you are dying, the DC of recovery checks is reduced by 1.

**Activate—True Love's Power** `pf2:r`

**Trigger** You would die due to a death effect rather than the dying condition

**Effect** Your love pulls you back from the brink of death and the locket cracks. You avoid dying and remain at 1 Hit Point. You cannot use the ability again until you replace the casing of the locket, which typically takes around 1 month and costs 600 gp.

*PFS Note:* Replacing the casing of a *locket of love left behind* takes 30 days of Downtime.

**Source:** `= this.source` (`= this.source-type`)
