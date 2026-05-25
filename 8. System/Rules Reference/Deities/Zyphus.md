---
type: deity
source-type: "Remaster"
domains: "Death, Sorrow, Soul, Undeath"
favored-weapon: "Pick"
divine-font: "Harm"
divine-skill: "Thievery"
divine-spells: "Rank 1: [[Ill Omen]], Rank 2: [[Shatter]], Rank 6: [[Phantasmal Calamity]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Legends say Zyphus rose from the soul of the first mortal to die from an accidental and meaningless death. These legends hold that when this soul appeared in Pharasma's Boneyard, he cursed the goddess and refused to accept her judgment, and instead escaped to become a god himself. The highest ranking among the Grim Harvestman's faith believe a darker truth: that Zyphus was and is the accident that killed this soul and all other mortals thereafter who befall fatal misfortune. Those who rail against their final judgment act out a final spiritual tragedy, the denial of the impartial force who might be their final defense against Zyphus's clutches. Those who cannot accept their unfortunate demises, it is said, turn their backs on life and are consumed by Zyphus, their souls forever gone from the cycle of life and death.

Whether this is true or simply a harrowing tale spread by worshippers of the cruel god to bolster terror is largely irrelevant, for the faithful of Zyphus are already reviled and feared. As devotees of the god of death and tragedy, they see death not as a natural end of life but as the punishment for daring to enjoy life at all. Many of these spiteful worshippers came to the faith as the result of an unfortunate tragedy capitalized upon (and often engineered by) other priests of Zyphus. Rather than healing and moving on, these individuals obsess over their misfortune and see inflicting tragedy on others as the only way to justify what happened to them. In time, such folk grow addicted to the cruelty, find pleasure in pain, and sup upon the tears of mourners while basking in their losses. In time, all worshippers of Zyphus become spite-filled wells of hatred whose long-standing grudges have bloomed into ceaseless drives to spread misery through the world.

**Title** The Grim Harvestman

**Areas of Concern** accidental death, graveyards, spite, tragedy

**Edicts** encourage deadly accidents by performing acts of sabotage or through faulty design, seek out instances of tragedy and foster ill will in the surviving victims, spread the belief that life is pointless since it all ends in the pain of death

**Anathema** engineer the same accident twice in a row, knowingly provide aid to a Pharasmin, spread hope or optimism (particularly in the face of a tragedy)

**Religious Symbol** pickaxe made of bones

**Sacred Animal** vulture

**Sacred Colors** ivory, red

**Source:** `= this.source` (`= this.source-type`)
