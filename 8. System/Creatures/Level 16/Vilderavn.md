---
type: creature
group: ["Fey"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Vilderavn"
level: "16"
rare_01: "Rare"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Fey"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+28; [[Greater Darkvision]], [[Truesight]] (precise) 60 feet"
languages: "Aklo, Common, Diabolic, Fey (Truespeech)"
skills:
  - name: Skills
    desc: "Acrobatics +30, Athletics +32, Deception +29, Society +24, Stealth +32, Heraldry Lore +26, Warfare Lore +26"
abilityMods: ["+8", "+6", "+5", "+4", "+4", "+7"]
abilities_top:
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Bloodbird"
    desc: "A creature hit by a vilderavn's melee attack becomes cursed. It takes 2d6 persistent bleed damage that's difficult to stanch. <br>  <br> The DC to stop the bleeding using [[Administer First Aid]] is 35, and healing the creature to full HP doesn't automatically end the bleeding. <br>  <br> Removing the curse ends the bleeding."
  - name: "Souleater"
    desc: "If the vilderavn kills a humanoid with a critical hit using their jaws Strike, they rip out and devour the target's heart and soul as part of the attack. <br>  <br> While the target is dead, the vilderavn can Change Shape into the target's form, gaining a +4 status bonus to Deception checks to impersonate the target. <br>  <br> If magic would resurrect the creature, the caster must succeed at a DC 34 counteract check to extract the target's soul from the vilderavn; otherwise, the spell fails."
armorclass:
  - name: AC
    desc: "40; **Fort** +25, **Ref** +30, **Will** +28"
health:
  - name: HP
    desc: "300; **Immunities** curse, death effects, drained, fear effects; **Weaknesses** cold iron 10"
abilities_mid:
  - name: "Aura of Disquietude"
    desc: "30 feet. DC 35 [[Will]] save <br>  <br> As [[Frightful Presence]], plus a creature frightened by the aura becomes suspicious; it doesn't count any other creature as its ally and can't [[Aid]] or flank. On a critical failure, the creature also can't be a willing target for harmless or helpful magic. <br>  <br> > [!danger] Effect: Aura of Disquietude <br>  <br> A creature that first enters the area must attempt a Will save. <br>  <br> Regardless of the result of the saving throw, the creature is temporarily immune to this monster's Frightful Presence for 1 minute. <br> - **Critical Success** The creature is unaffected by the presence. <br> - **Success** The creature is [[Frightened]] 1. <br> - **Failure** The creature is [[Frightened]] 2. <br> - **Critical Failure** The creature is [[Frightened]] 4."
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Greatsword +34 (`pf2:1`) (magical, versatile p), **Damage** 3d12+16 slashing plus [[Bloodbird]]"
  - name: "Melee strike"
    desc: "Jaws +32 (`pf2:1`) (magical, unarmed), **Damage** 3d8+16 piercing plus [[Bloodbird]]"
  - name: "Melee strike"
    desc: "Talon +32 (`pf2:1`) (agile, magical, unarmed), **Damage** 3d8+16 slashing plus [[Bloodbird]]"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 37, attack +29<br>**6th** [[Truesight]] (Constant)<br>**5th** [[Truespeech]] (Constant), [[Wave of Despair (At will)]]<br>**4th** [[Outcast's Curse (At will)]], [[Rewrite Memory]], [[Suggestion]], [[Suggestion (At will)]], [[Translocate]]"
abilities_bot:
  - name: "Change Shape"
    desc: "`pf2:1` The vilderavn takes on the appearance of a Small or Medium humanoid, wolf, dire wolf, or hybrid with both raven and wolf parts. The vilderavn can only use their jaws attack when in a form with a wolf's head, and their talon attack in a form with raven qualities. They can instead assume their raven knight form: a Medium humanoid in black full plate carrying a greatsword. They can use their jaws or talon Strikes only in a form that has that body part, and their greatsword only in knight form. <br>  <br> The monster changes its shape indefinitely. It can use this action again to return to its natural shape or adopt a new shape. Unless otherwise noted, a monster cannot use Change Shape to appear as a specific individual. Using Change Shape counts as creating a disguise for the [[Impersonate]] use of Deception. The monster's transformation automatically defeats Perception DCs to determine whether the creature is a member of the ancestry or creature type into which it transformed, and it gains a +4 status bonus to its Deception DC to prevent others from seeing through its disguise. Change Shape abilities specify what shapes the monster can adopt. The monster doesn't gain any special abilities of the new shape, only its physical form. For example, in each shape, it replaces its normal Speeds and Strikes, and might potentially change its senses or size. Any changes are listed in its stat block."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

In their true form, a vilderavn is a great raven with a wingspan of 6–8 feet. Adaptable shapeshifters, they can change to the fighting forms of a snarling wolf, a hybrid of both wolf and raven, and a tall humanoid in black armor with a massive greatsword. More sinister is their ability to assume a humanoid guise suited to insinuating themselves into the retinues of boastful mortal rulers. With historical knowledge and clever rumormongering, they goad the proud into squabbles, feuds, and ultimately wars. The vilderavn stays at the ruler's side until victory is within grasp, the war almost won, then exacts the cruel stroke of betrayal. Their magic turns the mortals against each other, and the vilderavn's sword falls swiftly.

```statblock
creature: "Vilderavn"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
