---
type: deity
source-type: "Remaster"
domains: "Destruction, Duty, Fire, Might"
favored-weapon: "Whip"
divine-font: "Harm"
divine-skill: "Athletics"
divine-spells: "Rank 1: [[Breathe Fire]], Rank 5: [[Acid Storm]], Rank 7: [[Fiery Body]]"
source: "Pathfinder #218: Titanbane"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

The general of Hell's armies, Moloch, embodies infernal discipline and incomparable destructive power. Across his ream of Malebolge, the sixth layer of Hell, the Ashen Bull trains countless legions of devils to wage unending war. He not only teaches obedience, he demands it, punishing every slightest misstep or insurrection with immediate, fiery retribution. Despite his harsh nature, Moloch is the most widely worshipped of the archdevils among mortals, as he is the most likely to answer supplicants' mundane pleas. In exchange, he asks only their souls to add to his endless armies—a price many are willing to pay.

**Title** The Ashen Bull

**Areas of Concern** Fire, obedience, war

**Edicts** Spread Hell's order through war, convert communities to sole worship of Moloch, sacrifice creatures in fire

**Anathema** Defy a military superior, flee in battle (unless ordered to do so), lose your combat edge due to your vices

**Religious Symbol** bull's head with flame

**Sacred Animal** bull

**Sacred Colors** orange, yellow

**Source:** `= this.source` (`= this.source-type`)
