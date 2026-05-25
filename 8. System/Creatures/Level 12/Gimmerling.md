---
type: creature
group: ["Fey"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Gimmerling"
level: "12"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Fey"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+21; [[Low-Light Vision]]"
languages: "Aklo, Common, Fey"
skills:
  - name: Skills
    desc: "Athletics +22, Crafting +23, Deception +25, Nature +21, Stealth +25, Thievery +25"
abilityMods: ["+4", "+7", "+4", "+5", "+3", "+4"]
abilities_top:
  - name: "Hungersense (Imprecise) 30 feet"
    desc: "Hungersense allows the gimmerling to sense creatures that require food to live."
  - name: "Sneak Attack"
    desc: "The gimmerling deals 2d6 extra precision damage to [[Off Guard]] creatures."
  - name: "Trickster's Step"
    desc: "The gimmerling ignores difficult terrain and doesn't trigger traps with its movement."
armorclass:
  - name: AC
    desc: "34; **Fort** +22, **Ref** +25, **Will** +19"
health:
  - name: HP
    desc: "235; **Weaknesses** cold iron 10"
abilities_mid:
  - name: "Treacherous Aura"
    desc: "15 feet. <br>  <br> Tangled roots, jagged divots, sharp rocks and other hazards appear on surfaces in the aura, creating difficult terrain."
  - name: "Trip Up"
    desc: "`pf2:r` **Trigger** A creature critically fails a melee attack to hit the gimmerling or moves into a space within the gimmerling's treacherous aura <br>  <br> **Effect** The triggering creature must attempt a DC 32 [[Reflex]] save. <br> - **Critical Success** The target is unaffected. <br> - **Success** The target is [[Off Guard]] until the start of its next turn. <br> - **Failure** The target takes 2d10 bludgeoning damage and is off-guard until the start of its next turn. <br> - **Critical Failure** As failure, and the target is knocked [[Prone]]."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +26 (`pf2:1`) (agile, finesse, unarmed), **Damage** 2d8+7 slashing plus [[Disarm]]"
  - name: "Melee strike"
    desc: "Jaws +26 (`pf2:1`) (finesse, unarmed), **Damage** 3d8+7 piercing plus 2d6 poison"
  - name: "Ranged strike"
    desc: "Hand Crossbow +28 (`pf2:1`) (reload 1, range 60 ft.), **Damage** 2d6+3 piercing plus 2d6 poison"
spellcasting: []
abilities_bot:
  - name: "Change Shape"
    desc: "`pf2:1` The gimmerling takes on the appearance of any humanoid. In humanoid form, They lose their treacherous aura, and their equipment appears to be trinkets or toys. If the chosen form lacks claws or fangs, they lose the matching Strike. If they lose their claw Strike, they gain a fist Strike that is identical except that it deals bludgeoning damage. <br>  <br> The monster changes its shape indefinitely. It can use this action again to return to its natural shape or adopt a new shape. Unless otherwise noted, a monster cannot use Change Shape to appear as a specific individual. Using Change Shape counts as creating a disguise for the [[Impersonate]] use of Deception. The monster's transformation automatically defeats Perception DCs to determine whether the creature is a member of the ancestry or creature type into which it transformed, and it gains a +4 status bonus to its Deception DC to prevent others from seeing through its disguise. Change Shape abilities specify what shapes the monster can adopt. The monster doesn't gain any special abilities of the new shape, only its physical form. For example, in each shape, it replaces its normal Speeds and Strikes, and might potentially change its senses or size. Any changes are listed in its stat block."
  - name: "Sly Disarm"
    desc: "`pf2:1` **Requirements** The gimmerling's last action was a successful claw Strike <br>  <br> **Effect** The gimmerling attempts to `act disarm options=sly-disarm` the creature they hit. They gain a +4 status bonus on the Athletics check. This attempt neither applies nor counts toward the gimmerling's multiple attack penalty."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Gimmerlings are small, shapeshifting fey who stage ambushes to sate their endless hunger and childish greed. These cruelly curious fey obsess over finding and making unusual traps and sadistic weapons, and their favorite amusement is seeing these traps sprung or the weapons wielded. When residing on Golarion, they're frequently found in urban areas, particularly slums or other parts of town, where they can either go unnoticed or be easily forgotten—and have plenty of victims to choose from.

A typical gimmerling disguises themself as an endangered child, hoping to draw creatures close enough to rob. The gimmerling puts themself in apparent danger using a trap, construct, a bribed ally, or even a coerced monster.

Because gimmerlings sometimes trade obscure smithing or trapping techniques in exchange for gifts that sate their curiosity, their greed, or their hunger, they have at times been worshipped as minor gods of the forge. Some disciplined gimmerlings work as honored artisans, elite guards, or spies for the demigods known as the Eldest, who dwell in the depths of the First World.

```statblock
creature: "Gimmerling"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
