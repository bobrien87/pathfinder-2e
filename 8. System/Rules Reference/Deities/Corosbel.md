---
type: deity
source-type: "Remaster"
domains: "Death, Secrecy, Soul, Trickery"
favored-weapon: "Dagger"
divine-font: "Harm, Heal"
divine-skill: "Deception"
divine-spells: "Rank 1: [[Charm]], Rank 4: [[Nightmare]], Rank 5: [[Subconscious Suggestion]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

At times, the greatest evils lurk within the gilded trappings of those who believe they are chosen by their gods. Corosbel seeks to further debase the souls of mortals who are convinced of their own self-righteousness. He also can be found in the poisoned hearts of religious servants who justify their heinous acts as payment for shepherding their flocks. This harbinger works slowly, for the best way to corrupt is to let prey remain thoroughly convinced that they are pure. It is said Corosbel's devotees never start out worshipping him directly. They claim that initially, whenever they prayed for the means to hide their debasements, divine messengers came to them in their dreams. By the time the truth is revealed, they are often too in love with their power for them to stop their own downfall.

**Title** The Silent Saint

**Areas of Concern** Failed martyrdom, false worship, religious corruption

**Edicts** Convert other faithful into lives of excess, take what is due to you as a divine messenger, tempt others into false worship

**Anathema** Deny yourself an opportunity to extort your flock, perform an act of true selflessness

**Religious Symbol** hand with broken fingers

**Sacred Animal** calf

**Sacred Colors** red, white

**Source:** `= this.source` (`= this.source-type`)
