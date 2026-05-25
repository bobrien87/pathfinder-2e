---
type: deity
source-type: "Remaster"
domains: "Family, Might, Passion, Protection"
favored-weapon: "Shield-boss"
divine-font: "Heal"
divine-skill: "Performance"
divine-spells: "Rank 1: [[Mindlink]], Rank 2: [[Laughing Fit]], Rank 6: [[Wall Of Force]]"
source: "Pathfinder #216: The Acropolis Pyre"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

When Upion received his myth-speaking, he politely thanked the cyclopes but refused to seek divinity or hear their whole prophecy. To do so would mean outliving his lover, Warrik, by decades or even centuries. Instead, the pair continued their military careers, believing it better to find immortality together on the front lines than chase some goal they couldn't share. Both appeared to perish in the Battle of Tesikon Heights, only to arise imbued with mythic power to turn the tide of battle. Since then, Upion and Warrik have acted as a single hero-god, seemingly able to grant spells only when together. The pair encourage camaraderie, neither expecting nor disparaging those whose loyalty develops into consensual romance.

**Title** The Shieldbrothers

**Areas of Concern** shield-bearers and promises

**Edicts** share stories that glorify your companions, guard your friends' backs, find joy in grim circumstances

**Anathema** betray a lover, flee battle before your companions have a chance to escape

**Religious Symbol** pair of overlapping circular shields

**Sacred Animal** wolf

**Sacred Colors** brown, orange

**Source:** `= this.source` (`= this.source-type`)
