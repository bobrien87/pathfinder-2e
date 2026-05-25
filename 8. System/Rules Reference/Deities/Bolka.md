---
type: deity
source-type: "Remaster"
domains: "Confidence, Family, Healing, Passion"
favored-weapon: "Mace"
divine-font: "Heal"
divine-skill: "Diplomacy"
divine-spells: "Rank 1: [[Soothe]], Rank 4: [[Creation]], Rank 6: [[Collective Transposition]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Bolka is the dwarven goddess of marriage. Forged by Torag as a symbol of his love for Folgrit, Bolka's golden-brown skin, eyes of pure bismuth, and honey-blonde hair were a symbol of the passion and beauty he saw in Folgrit. When Folgrit received this gift, she immediately breathed life into the child, and claimed Bolka to be a symbol of their marriage and eternal commitment.

Bolka's beauty is without equal among the dwarven gods. She has many suitors, and those who would try to win her hand with feats of strength or bravery. She is grateful for this attention, but with a small kiss on the cheek and a touch on the arm, she tells all of them that she's too busy working to commit to family at the moment. She tirelessly strives toward helping dwarven suitors find the confidence and strength to confess love and devotion to potential partners.

**Title** The Golden Gift

**Areas of Concern** Committed relationships, marriage, passion

**Edicts** Encourage those seeking love, see the beauty in others, support others' relationships

**Anathema** Betray your spouse, disrupt a genuine marriage, prevent a suitor from seeking a partner

**Religious Symbol** wedding bells

**Sacred Animal** falcon

**Sacred Colors** gold, green

**Source:** `= this.source` (`= this.source-type`)
