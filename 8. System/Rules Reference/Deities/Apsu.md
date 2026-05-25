---
type: deity
source-type: "Remaster"
domains: "Creation, Dragon, Protection, Travel"
favored-weapon: "Jaws, Staff"
divine-font: "Heal"
divine-skill: "Diplomacy"
divine-spells: "Rank 1: [[Anticipate Peril]], Rank 4: [[Creation]], Rank 5: [[Summon Dragon]], Rank 9: [[Falling Stars]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Texts more ancient than recorded time kept in the halls of draconic sages assert that Apsu and his mate Sarshallatu were the first dragons. The two spawned seven children and as a family, they shaped the mortal world of Golarion. However, one of these children broke Apsu's heart during that time. Instead of wanting to create, his child, named Dahak, sought only to destroy. As much as it pained Apsu to fight his child, he could not let this world be destroyed senselessly, but when Apsu had gained the upper hand, his partner stopped him. Dahak then fled to Hell to nurse his wounds.

To this day, Apsu continues to battle against the forces that seek to destroy this world, forever reminded of his failure to stop his child and the pain of Sarshallatu's betrayal. Though he strives for peace, he knows that one day, he will have to confront Dahak once again and that all dragonkind will be involved in the inevitable conflict. Such a war would sweep across Golarion like a massive wildfire. Until that time, Apsu entreats mortal artists and leaders to make the world the best place it can possibly be. Somewhat ironically, when Apsu contemplates these acts of beauty and harmony, he grows ever more despondent about his fated battle against his son.

**Title** The Waybringer

**Areas of Concern** leadership, peace, virtuous dragons

**Edicts** seek and destroy evil, travel the world, help others fend for themselves

**Anathema** fail to pursue a foe who has betrayed your mercy, attack a creature without certainty of wrongdoing

**Religious Symbol** silvery dragon above a mirrored pool

**Sacred Animal** none

**Sacred Colors** gold, silver

**Source:** `= this.source` (`= this.source-type`)
