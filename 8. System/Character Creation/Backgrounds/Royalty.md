---
type: background
source-type: "Remaster"
boosts: "Cha/Int, Cha/Con/Dex/Int/Str/Wis"
skills: "Society"
feats: "[[Courtly Graces]]"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You are a prominent member of a royal family. You have eschewed the daily routines of royal life and taken up an adventurous quest—perhaps you're a deposed queen hoping to regain her throne, a prince seeking a more exciting life, or a sovereign's heir on a secret mission.

Choose two attribute boosts. One must be to **Intelligence** or **Charisma**, and one is a free attribute boost.

You are trained in Society. You gain the [[Courtly Graces]] skill feat and can influence commoners in your family's territory, as well as nobility anywhere. If you later gain the [[Leverage Connections]] skill feat, you automatically have common and noble connections within any community in your royal family's territory and have noble connections in large communities outside your territory.

**Source:** `= this.source` (`= this.source-type`)
