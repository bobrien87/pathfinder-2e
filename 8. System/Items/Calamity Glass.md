---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Cursed]]", "[[Magical]]", "[[Scrying]]"]
price: "{'value': {}}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This mirror appears to give warnings about the future, but subtle and malevolent hands designed the silver-framed glass to lure heroes into bringing doom upon those they hope to save.

**Activate—Mirror, Mirror** 1 minute (concentrate, manipulate)

**Frequency** once per week

**Effect** You activate the *calamity glass* and obtain a vision related to a likely action or event within the next 48 hours. The *calamity glass* decides what vision to show, though if you think about a specific event, the vision is typically at least tangentially related.

No matter what, the mirror shows only tragedies. The mirror's visions are accurate but misleading, as they depict tragedies that could be averted but in so doing might lead to greater suffering.

For example, a *calamity glass* might show a family starving as the result of harbor officials turning away a boatload of improperly documented grain. Without intervention, this future will come to pass. What the mirror didn't show is the grain was improperly labeled and carelessly stored, resulting in its contamination with poisonous mold capable of killing hundreds. Purifying and then distributing the grain would avert both the *calamity glass'*s vision and the greater suffering its curse attempted to create.

**Source:** `= this.source` (`= this.source-type`)
