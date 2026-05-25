---
type: creature
group: ["Amphibious", "Beast"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Ahuizotl"
level: "6"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Amphibious"
trait_02: "Beast"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+14; [[Darkvision]]"
languages: "Aklo, Common"
skills:
  - name: Skills
    desc: "Athletics +15, Deception +15, Stealth +15"
abilityMods: ["+5", "+3", "+5", "-1", "+3", "+3"]
abilities_top:
  - name: "Voice Imitation"
    desc: "An ahuizotl can mimic the sounds of a person in distress by attempting a Deception check to `act lie options=voice-imitation` The ahuizotl has a +4 circumstance bonus to this check."
armorclass:
  - name: AC
    desc: "23; **Fort** +17, **Ref** +13, **Will** +13"
health:
  - name: HP
    desc: "105"
abilities_mid:
  - name: "Improved Grab"
    desc: "`pf2:0` **Trigger** The monster's last action was a successful Strike that lists Improved Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with as a free action. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Improved Grab as an action and choose one creature it's grabbing or restraining with an appendage that has Improved Grab to automatically extend that condition to the end of the monster's next turn."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +17 (`pf2:1`) (unarmed), **Damage** 2d8+8 piercing"
  - name: "Melee strike"
    desc: "Claw +17 (`pf2:1`) (agile, unarmed), **Damage** 2d6+8 slashing"
  - name: "Melee strike"
    desc: "Tail Claw +17 (`pf2:1`) (agile, reach 10 ft.), **Damage** 2d4+8 slashing plus [[Improved Grab]]"
spellcasting: []
abilities_bot:
  - name: "Tail Drag"
    desc: "`pf2:1` **Requirements** The ahuizotl has a Medium or smaller creature grabbed with its tail claw <br>  <br> **Effect** The ahuizotl attempts an [[Athletics]] check against the creature's Fortitude DC. <br> - **Critical Success** If the creature is 10 feet away from the ahuizotl, it is dragged into a square adjacent to the ahuizotl. The ahuizotl can make a jaws Strike against the creature. <br> - **Success** If the creature is 10 feet away from the ahuizotl, it is dragged into a square adjacent to the ahuizotl. <br> - **Failure** The creature is not dragged. <br> - **Critical Failure** The creature is not dragged and the ahuizotl no longer has the creature grabbed."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

The ahuizotl is a vicious, semiaquatic predator that resembles a hideous cross between a badger and an otter, with disturbingly web-fngered paws supplemented by a ffth hand at the end of a long, serpentine tail. A clever and stealthy hunter, the ahuizotl lures unwary prey to their doom by mimicking the cries of people in distress. The hand on an ahuizotl's tail is surprisingly strong, and the creatures tend to use their tails to ambush potential victims. The ahuizotl's macabre habit of feeding on a victim's eyes, fngernails, and teeth leaves the corpses of their kills uniquely mutilated. Some say the creatures consider these body parts delicacies, while others insist ahuizotls collect them as tribute to a powerful but unknown entity. The fact that an ahuizotl doesn't eat the actual fesh of their victims, instead depositing their savaged and waterlogged corpses in locations where the remains are sure to be found by friends or family, points to a third and perhaps more likely possibility—the ahuizotl simply enjoys using their violent dietary quirks to spread fear and despair.

An ahuizotl walks on all fours, but their hands are capable of manipulating simple tools and other objects. Ahuizotls have roughly mustelid features and an extra membrane covering their eyes, giving their eyes a dull color suggestive of cataracts and somewhat blunting the creature's vision. Yet despite their bestial appearance, ahuizotls are nearly as intelligent as the average human, and wiser than most. Although they don't form societies of their own, they've been known to ally with violent cults or conclaves of monsters, and even to found small shrines and temples to sinister deities. The cult of Charon, the Apocalypse Rider of Death, is particularly popular among certain ahuizotls, who look forward to an afterlife spent wallowing in the waters of the River Styx.

```statblock
creature: "Ahuizotl"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
