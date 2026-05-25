---
type: deity
source-type: "Remaster"
domains: "Confidence, Darkness, Sorrow, Travel"
favored-weapon: "Rapier"
divine-font: "Harm, Heal"
divine-skill: "Stealth"
divine-spells: "Rank 1: [[Penumbral Shroud]], Rank 4: [[Peaceful Bubble]], Rank 5: [[Umbral Journey]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Once the lord of darkness and of the chaos of creation, Count Ranalc was cast out long ago by the other Eldest and titled "the Traitor," though the Eldest are not forthcoming about what heinous treachery Ranalc committed, and many among his worshippers claim that he was the one who was betrayed. In his new home in a remote corner of the Netherworld, Ranalc embraced his banishment and became the patron of exiles, shadows, betrayal, and the betrayed. Ranalc had long held a fascination with the world of Golarion, and he was alternately both friend and foil to the powerful archwizard Nex. On the day Nex besieged the city of Absalom with shadowy beings—beings certainly drawn from Ranalc's domain—the Eldest vanished from reality. Although he continues to grant spells to his devout worshippers, Ranalc has otherwise wholly disappeared. Theories about his disappearance abound, although they are as obscure and as self-contradictory as the enigmatic Eldest ever was.

**Title** The Traitor

**Areas of Concern** Betrayal, exiles, shadows

**Edicts** Work in shadows, hide your nature and motives, plot betrayals or revenge for betrayals

**Anathema** Ask for forgiveness, create permanent or long-lasting sources of light

**Religious Symbol** eye with crescent moon pupil

**Sacred Animal** bat

**Sacred Colors** black, gray

**Source:** `= this.source` (`= this.source-type`)
