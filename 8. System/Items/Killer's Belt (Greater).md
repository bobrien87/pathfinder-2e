---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 650}"
usage: "wornbelt"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Small blood-red rubies decorate this black leather belt, which is a fashion accessory for only the most bloodthirsty soldiers. When you wear this belt, you gain a +2 item bonus to Intimidation checks.

**Activate—Bleeding Rubies** `pf2:1` (manipulate)

**Frequency** once per day

**Requirements** You have a free hand and your last action was to deal damage to an enemy with a Strike or spell attack roll

**Effect** You pull a ruby off your belt and crush it into dust. As this dust reaches the enemy you just harmed, it embeds into the skin, causing them to bleed. The target takes 2d6 persistent,bleed damage. The ruby reappears on the belt after 24 hours.

**Source:** `= this.source` (`= this.source-type`)
