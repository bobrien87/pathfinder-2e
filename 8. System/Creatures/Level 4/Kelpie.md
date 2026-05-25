---
type: creature
group: ["Amphibious", "Fey"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Kelpie"
level: "4"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Amphibious"
trait_02: "Fey"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+11; [[Low-Light Vision]]"
languages: "Common, Fey, Thalassic"
skills:
  - name: Skills
    desc: "Athletics +11, Deception +14, Stealth +10"
abilityMods: ["+5", "+2", "+3", "-1", "+3", "+4"]
abilities_top: []
armorclass:
  - name: AC
    desc: "21; **Fort** +11, **Ref** +12, **Will** +14"
health:
  - name: HP
    desc: "60; **Weaknesses** cold iron 5; **Resistances** fire 5"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +13 (`pf2:1`) (unarmed), **Damage** 2d6+7 bludgeoning plus [[Grab]]"
spellcasting: []
abilities_bot:
  - name: "Captivating Lure"
    desc: "`pf2:2` The kelpie instills an overwhelming attraction to itself within the mind of a single creature within 60 feet. The target perceives the kelpie as a desirable person (if the kelpie is in humanoid form) or a magnificent steed (if the kelpie is in equine form) and must attempt a DC 23 [[Will]] save saving throw. <br> - **Critical Success** The creature is unaffected and is temporarily immune to Captivating Lure for 24 hours. <br> - **Success** The creature is [[Stupefied 1]] for 1 round and is then temporarily immune to Captivating Lure for 24 hours. <br> - **Failure** The creature is [[Fascinated]], and it must spend each of its actions to move closer to the kelpie as expediently as possible while avoiding obvious dangers. If a captivated creature is adjacent to the kelpie, it either attempts to mount the kelpie (if the kelpie is in equine form) or stays still and doesn't act. If the creature is attacked by the kelpie, or if it can't breathe water and enters an area of water, the creature is freed from captivation at the end of the kelpie's turn. <br> - **Critical Failure** As failure, but the target doesn't consider water a danger and will enter an area of water even if it can't swim or breathe water. If it is attacked by the kelpie or starts to drown, it can attempt a new save at the start of its next turn, but it isn't freed automatically."
  - name: "Change Shape"
    desc: "`pf2:1` The kelpie can take on the appearance of any Medium or Large animal of an equine nature (such as a Horse, [[Hippocampus]], or Pony), or any Small or Medium humanoid. This doesn't change its Speeds or its attack and damage modifiers with its Strikes. <br>  <br> The monster changes its shape indefinitely. It can use this action again to return to its natural shape or adopt a new shape. Unless otherwise noted, a monster cannot use Change Shape to appear as a specific individual. Using Change Shape counts as creating a disguise for the [[Impersonate]] use of Deception. The monster's transformation automatically defeats Perception DCs to determine whether the creature is a member of the ancestry or creature type into which it transformed, and it gains a +4 status bonus to its Deception DC to prevent others from seeing through its disguise. Change Shape abilities specify what shapes the monster can adopt. The monster doesn't gain any special abilities of the new shape, only its physical form. For example, in each shape, it replaces its normal Speeds and Strikes, and might potentially change its senses or size. Any changes are listed in its stat block."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Kelpies are malevolent, amphibious fey shapechangers who lure mortals to a watery grave. These cruel predators lurk around bodies of water of any type, only slightly preferring fresh water over salt water. Kelpies lure or drag their prey underwater, then drown and devour them, leaving behind only the victim's heart and liver—the only parts of a meal kelpies find unpleasant—tossed upon the shore. Kelpies are fond of magically disguising themselves as fine steeds or attractive strangers to draw in victims, but their true appearance is that of a hideous equine with slimy, green flesh resembling aquatic plants.

```statblock
creature: "Kelpie"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
