---
type: item
source-type: "Remaster"
level: "16"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 9000}"
usage: "worn"
bulk: "—"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Military leaders or heads of state award these special medals to commend exemplary performance by their top soldiers. They're typically worn on a special strip of fabric near the lapel, but soldiers from different countries sometimes wear them in other places. No matter how many magical medals you have, they collectively count as one invested item.

The phoenix on this gold medal is proud and fierce, and the medal features a border shaped like a flame. This medal is considered the highest honor in many countries and is awarded to those soldiers who have truly exemplified the ethics of their country through unbelievable service.

**Activate—Phoenix's Sacrifice** `pf2:f` (vitality)

**Frequency** once per day

**Trigger** Your [[Dying]] condition increases

**Effect** The phoenix bursts into flames. You lose the dying condition and regain @Damage[1[healing,vitality]|traits:vitality]{1 Hit Point}. Your [[Wounded]] value does not increase. You can use this action while [[Unconscious]].

**Source:** `= this.source` (`= this.source-type`)
