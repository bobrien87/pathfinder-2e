---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Intelligent]]", "[[Magical]]", "[[Primal]]", "[[Staff]]", "[[Two hand d8]]"]
price: "{'gp': 0}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Perception** +25; precise vision (low-light) 60 feet, imprecise hearing 30 feet, imprecise tremorsense 30 feet (only when touching the ground)

**Communication** speech (Arboreal, Common, Fey; *speak with plants*)

**Skills** Diplomacy +22, Forest Lore +25, Nature +25

**Int** +4, **Wis** +6, **Cha** +4

**Will** +27

Rather than passing on when they feel their death approaching, a rare few elderly arboreals undergo a ritual of preservation. This rite fuses the arboreal's consciousness into a branch, allowing their spirit to live on within the object. The branch functions as a greater verdant staff, though the arboreal spirit allows only partners willing to safeguard nature to use the staff's spells. An arboreal who decides to become an *arboreal staff* is more connected to shorter-lived species than others of their kind. Most choose to endure to share their knowledge with future generations, but they take a long view in ways that can be frustrating to their wielders.

In addition to the activation and spells of a *greater verdant staff*, an *arboreal staff* can cast the spells it holds as if it were the staff's wielder, though it usually does so only to benefit a partner. The staff also has *earthbind* available as a 3rd-rank spell.

**Activate** Cast a Spell

**Effect** You expend a number of charges from the staff to cast a spell from its list.

- **Cantrips** [[Tangle Vine]]
- **1st** [[Runic Body]], [[Runic Weapon]]
- **2nd** [[Entangling Flora]], [[Oaken Resilience]], [[One with Plants]], [[Shape Wood]]
- **3rd** [[Wall of Thorns]], [[Speak with Plants]], [[Earthbind]]
- **4th** [[Oaken Resilience]], [[Speak with Plants]]
- **5th** [[Plant Form]], [[Wall of Thorns]]

**Source:** `= this.source` (`= this.source-type`)
