---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Air]]", "[[Magical]]"]
price: "{'gp': 500}"
usage: "held-in-one-hand"
bulk: "5"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These magical platforms are used in a variety of performances. They allow performers to access high places safely, while also serving an important role before the performance even begins. They're used by various backstage crews to hang lights, curtains, and scenery above the stage. Sometimes several of these platforms are lined up to make an upper and lower stage. This large 10-foot-by-10-foot platform can be secured to a surface as a 1-minute activity. While standing on a secured platform, any creature can use the Adjust Height activation.

**Activate—Adjust Height** `pf2:1` (manipulate)

**Effect** The platform and all creatures and items on the platform either rise or lower up to 10 feet. This action fails if there is more than 50 Bulk on the platform.

**Source:** `= this.source` (`= this.source-type`)
