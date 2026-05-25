---
type: item
source-type: "Remaster"
level: "4"
price: "{'gp': 300}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Adventure Path: Hellbreakers"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This satirical play by Amalia Wraxton was published in 4710 ar. Its controversial content, depicting the eponymous queen as the lover of Asmodeus and a coconspirator in the death of Aroden, caused an uproar that led to violent suppression and a defiant uprising. The play has since been banned and can be found only among the secret collections of art connoisseurs. If you own a copy of this play, you can publicly perform parts of Abrogail I as a downtime activity with a successful DC 19 Performance check. This activity lasts four hours including setup, rehearsal, and attracting a crowd, and you can't perform this play again in this settlement for a week.
- **Critical Success** As success, but you gain 2 Uprising Points.
- **Success** The people are roused by your performance. You gain 1 Uprising Point.
- **Failure** The authorities crack down on rebellious activity, stopping you from performing in this settlement again for 1 month.
- **Critical Failure** As failure, but the people are intimidated and you lose 1 Uprising Point.

**Source:** `= this.source` (`= this.source-type`)
