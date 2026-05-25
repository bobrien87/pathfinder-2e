---
type: deity
source-type: "Remaster"
domains: "Healing, Protection, Repose, Vigil"
favored-weapon: "Light-mace"
divine-font: "Heal"
divine-skill: "Diplomacy"
divine-spells: "Rank 1: [[Soothe]], Rank 4: [[Liminal Doorway]], Rank 7: [[Contingency]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

While the chaotic roar of a battlefield isn't where most healers would choose to ply their trade, for worshippers of Dalenydra it's the perfect place. They are most often found working to save those who are injured in battle, and their religious symbols are a sign of neutrality to all involved. Those who recognize the regalia of her mortal servants go out of their way to protect them on the battlefield, even if they arrived with the opposing force, for they know that these medics see not the side a person is fighting on but their needs as a patient. Dalenydra appears as a woman with bronze skin, dark hair kept in a network of elaborate braids, and six arms, each holding a different healing tool or supplement. She often disguises herself to join her medics, as she is most at home helping those on the battlefield rather than sitting safe in some lofty corner of the upper planes, and takes on an appearance to match her followers and better fit in.

**Title** The Blessed Attendant

**Areas of Concern** Battlefield healing, caregiving, sanctuaries

**Edicts** Help those that are injured in battle, protect the innocent, care for others who cannot take care of themselves, attempt to solve conflicts diplomatically

**Anathema** Strike first in battle, let someone die on a battlefield without attempted intervention, cause the intended death of another

**Religious Symbol** bandage-wrapped fist

**Sacred Animal** silkworm

**Sacred Colors** red, white

**Source:** `= this.source` (`= this.source-type`)
