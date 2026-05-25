---
type: deity
source-type: "Remaster"
domains: "Family, Trickery, Tyranny, Delirium"
favored-weapon: "Crossbow"
divine-font: "Harm, Heal"
divine-skill: "Deception"
divine-spells: "Rank 1: [[Agitate]], Rank 3: [[Enthrall]], Rank 7: [[Warp Mind]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

The Chains and the Cradle is mother to all petitioners who cannot seem to let their beloved offspring go, whether they are born from their own wombs, adopted children, or students under their care. She corrupts the complicated emotions that come with watching someone one cares about grow strike out on their own, and revels in the often-unspoken fear of being left behind by those who once looked to us for guidance. Laivatiniel insists that control is the ultimate form of love and devotion, which often drives her followers to commit selfish acts against those whom they are supposed to protect. After all, what good is a baby bird that flies too far from their nest?

**Title** The Chains and the Cradle

**Areas of Concern** Anxiety, coddling, smothering parental love

**Edicts** Allow anxiety and jealousy to rule your actions, impose your will upon those who see you as a parental figure, usurp praise given to others for actions you may have suggested

**Anathema** Cede authority to another guardian, heed advice from your child or charge, ignore an opportunity to remind your charge of their place

**Religious Symbol** rattle wrapped in chains

**Sacred Animal** bear

**Sacred Colors** black, brown

**Source:** `= this.source` (`= this.source-type`)
