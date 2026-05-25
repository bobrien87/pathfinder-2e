---
type: creature
group: ["Beast"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Skull Peeler"
level: "6"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Beast"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+17; [[Low-Light Vision]]"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +12, Athletics +15, Stealth +16"
abilityMods: ["+5", "+4", "+3", "-3", "+3", "+1"]
abilities_top:
  - name: "Anticoagulant"
    desc: "The skull peeler's razor-sharp tongue is coated in an anticoagulant substance that makes wounds it inflicts particularly hard to close. <br>  <br> The DC of the flat check to end the persistent bleed damage from a skull peeler's tongue Strike is 16, or 11 with appropriate assistance."
armorclass:
  - name: AC
    desc: "24; **Fort** +13, **Ref** +16, **Will** +11"
health:
  - name: HP
    desc: "75"
abilities_mid:
  - name: "Snatch Skull"
    desc: "`pf2:r` **Trigger** The skull peeler is using Perfect Camouflage, and a creature moves into a space within 15 feet of it <br>  <br> **Effect** The skull peeler Leaps toward the triggering creature and Strikes with its tongue. If this Strike is successful, the skull peeler automatically Grabs the target with its tongue."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Tongue +17 (`pf2:1`) (agile, fatal d12, reach 10 ft.), **Damage** 2d4+8 slashing plus 1d8 bleed"
  - name: "Melee strike"
    desc: "Claw +17 (`pf2:1`), **Damage** 2d10+8 slashing"
spellcasting: []
abilities_bot:
  - name: "Perfect Camouflage"
    desc: "`pf2:1` **Requirements** The skull peeler is in a treetop or standing on a tree limb <br>  <br> **Effect** Until the next time it acts, the skull peeler hangs perfectly still, blending into the treetop surroundings. It has an automatic result of 36 on Stealth checks and DCs to Hide from any creature more than 10 feet away from it."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Skull peelers, despite their ferocious and well-deserved moniker, are considered by many to be downright adorable, especially when viewed from a safe distance. Their soft, dappled brown fur helps them hide in forest canopies, and they have shimmering insectile wings and big eyes that draw in the faintest beams of light. At first glance, a skull peeler looks like a cuddly pet or a wizard's familiar. Any illusions of domesticating such a beast are quickly dismissed upon seeing how a skull peeler eats, however.

Skull peelers have evolved to hang motionlessly in treetop canopies as they wait until appropriate prey appears, usually long-necked dinosaurs but also brachiating primates and large birds. The skull peeler then lashes out with its long tongue, severing the creature's head from its body and pulling the detached cranium back into its hungry paws. It then uses its claws to crack open the cranial cavity—hence its name—before lapping up the tasty insides.

Despite skull peelers' gruesome eating habits, some enterprises and individuals can't resist the urge to add these beasts to their menageries. Fey and other creatures with ties to the First World, such as gnomes, can occasionally coax a skull peeler into a form of domestication. While the adorable beasts can never be fully tamed due to their hyper-evolved hunting instincts, they can be bribed with food and, if kept satiated, displayed on a perch or indoor terrarium as an example of their master's cunning and deadliness. As often as not, these pseudo-domesticated skull peelers end up devouring a guest, pet, or their would-be owner, but this possibility doesn't stop up-and-coming crime lords from attempting to tame the little predators. Skull peelers kept in well-managed zoos fare somewhat better, but these clever creatures don't always stay in their cages, which has led to wild skull peelers in places travelers might not expect.

```statblock
creature: "Skull Peeler"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
