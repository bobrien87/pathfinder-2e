---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 150}"
usage: "worn"
bulk: "L"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This woven shawl changes its color, material, and abilities with the seasons. In its usual state, it reflects the current season of the environment the wearer is in. The handsome embroidery grants you a +2 item bonus to Diplomacy checks to [[Make an Impression]].

**Activate—Change of Seasons** 10 minutes (concentrate)

**Frequency** once per day

**Effect** You arrange the shawl on your shoulders to gain the benefits of a season of your choice until your next daily preparations. If the season you choose is the current season, you also gain a +1 item bonus to Fortitude saving throws.

- **Spring** The shawl becomes smooth silk covered in delicate flowers. You gain a +5-foot item bonus to your Speed.
- **Summer** The shawl becomes light cotton with the hues of fresh grass. You're protected from the effects of severe heat.
- **Fall** The shawl becomes thin leather with an ombre of red and orange leaves. You treat falls as 10 feet shorter.
- **Winter** The shawl becomes warm wool as white as snow. You're protected from the effects of severe cold.

**Source:** `= this.source` (`= this.source-type`)
