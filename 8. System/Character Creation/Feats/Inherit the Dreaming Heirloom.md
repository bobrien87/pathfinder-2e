---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Wayang]]"]
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Whether you always carried it or perhaps only recently inherited, you have a pusaka—an heirloom containing a spirit who you communicate with in your dreams. Choose one item of light Bulk to be your pusaka. It becomes a magic item that has the occult trait. As long as you sleep with this item in reach and spend 10 minutes during your daily preparations pampering the spirit within, you can Activate the pusaka that day.

**Activate—Ancestral Recollection** `pf2:1` (concentrate)

**Frequency** once per day

**Effect** The spirit within the pusaka advises you on a subject they knew in life. When you gain this feat, select one Lore skill about a profession and one about a type of environment, such as Accounting Lore and Forest Lore. When you Activate the pusaka, you attempt to Recall Knowledge using one of these skills (you become temporarily trained in these skills for this check). Once you make your choice of Lore skills, they can't be changed.

**Activate—Guide My Dreams** `pf2:2` (concentrate)

**Effect** You ask the spirit within the pusaka to show you the way. You cast [[Guidance]] as an occult cantrip. A cantrip is heightened to a spell rank equal to half your level rounded up.

**Source:** `= this.source` (`= this.source-type`)
