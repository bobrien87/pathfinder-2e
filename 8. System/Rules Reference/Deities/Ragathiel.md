---
type: deity
source-type: "Remaster"
domains: "Destruction, Duty, Fire, Zeal"
favored-weapon: "Bastard-sword"
divine-font: "Harm, Heal"
divine-skill: "Intimidation"
divine-spells: "Rank 1: [[Sure Strike]], Rank 3: [[Haste]], Rank 4: [[Fire Shield]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

The General of Vengeance presides over chivalry, duty, and vengeance, acting as the quintessential knight. Born of the archdevil Dispater and Feronia, a demigoddess of fire, Ragathiel struggles to overcome the reputation of his parentage, and he understands the struggle to be accepted, to be trusted, and to fight against his own nature for the sake of good. He represents strength in battle, wrath upon the wicked, absolution or vengeance for the wronged, leadership when needed, and virtue and duty to the innocent. He expects his followers to destroy fiends when they find them and to work toward truly earning the trust and acceptance of those around them. Those who follow him lead by shining example and can be found on the front lines of battle or any conflict against evil they can find.

**Title** General of Vengeance

**Areas of Concern** Chivalry, duty, vengeance

**Edicts** Avenge the wronged, destroy evildoers, lead the charge in battle

**Anathema** Cower from combat, forgive those who have irreparably sinned, leave allies unwillingly in darkness

**Religious Symbol** sword crossed with wing

**Sacred Animal** mastiff

**Sacred Colors** crimson, gold

**Source:** `= this.source` (`= this.source-type`)
