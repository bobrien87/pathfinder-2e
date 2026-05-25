---
type: deity
source-type: "Remaster"
domains: "Ambition, Destruction, Fire, Might"
favored-weapon: "Greatsword"
divine-font: "Harm"
divine-skill: "Athletics"
divine-spells: "Rank 1: [[Breathe Fire]], Rank 3: [[Haste]], Rank 4: [[Weapon Storm]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

All Szuriel has ever known is war. In life she was first a champion of justice, then excommunicated from her church for heresy. In response, she slaughtered her way to power until she was crowned empress, then subsequently had every member of her former faith crucified. She went on to wage several brutal wars against neighboring kingdoms until an assassin's dagger found her heart. Sent to Abaddon, she rose quickly through the ranks of daemonkind, and when she saw weakness in the Rider of War, she slew him in battle, claiming his title for herself.

**Title** Angel of Desolation

**Areas of Concern** War

**Edicts** End all mortal life through war, obliterate faith

**Anathema** Show mercy to creatures who do not worship Szuriel, choose to marry or have children

**Religious Symbol** Pale hand and black sword

**Sacred Animal** horse, vulture

**Sacred Colors** red

**Source:** `= this.source` (`= this.source-type`)
