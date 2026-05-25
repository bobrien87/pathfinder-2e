---
type: creature
group: ["Asura", "Spirit"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Garadasura"
level: "11"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Asura"
trait_02: "Spirit"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+21; [[Darkvision]]"
languages: "Common, Diabolic (Telepathy 60 feet)"
skills:
  - name: Skills
    desc: "Acrobatics +21, Athletics +23, Intimidation +21, Performance +21, Religion +21, Stealth +23"
abilityMods: ["+6", "+3", "+6", "+0", "+2", "+4"]
abilities_top:
  - name: "Telepathy 60 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Butchering Venom"
    desc: "**Saving Throw** DC 30 [[Fortitude]] save <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** 3d6 poison damage and [[Slowed]] 1 (1 round) <br>  <br> **Stage 2** 4d6 poison damage and [[Slowed]] 2 (1 round) <br>  <br> **Stage 3** 6d6 poison damage and [[Paralyzed]] for 1 hour"
armorclass:
  - name: AC
    desc: "30; **Fort** +24, **Ref** +20, **Will** +19"
health:
  - name: HP
    desc: "200; **Immunities** curse, disease, poison"
abilities_mid:
  - name: "Fast Healing 5"
    desc: "A monster with this ability regains the given number of Hit Points each round at the beginning of its turn."
  - name: "Encircling Aura"
    desc: "50 feet. A garadasura exudes a 50-foot aura whenever it remains motionless for at least 1 round. If the garadasura has the holy trait, all allied creatures within the area gain a +1 status bonus to AC and saving throws. If the garadasura has the unholy trait, all unallied creatures that enter this area must succeed at a DC 30 [[Will]] save or spend their next action to move toward the garadasura's location. If the garadasura moves, the efect ends for all currently affected creatures."
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Scimitar +24 (`pf2:1`) (forceful, magical, reach 10 ft., sweep), **Damage** 2d6 poison plus 1d6 spirit plus 2d6+9 slashing"
  - name: "Melee strike"
    desc: "Fangs +24 (`pf2:1`) (agile), **Damage** 1d6 spirit plus 2d6+9 piercing plus [[Butchering Venom]]"
  - name: "Melee strike"
    desc: "Tail +24 (`pf2:1`) (agile, reach 15 ft.), **Damage** 2d6+9 bludgeoning plus 1d6 spirit plus [[Grab]]"
  - name: "Ranged strike"
    desc: "Venom Spit +28 (`pf2:1`) (agile), **Damage** 2d6+6 poison plus [[Butchering Venom]]"
spellcasting: []
abilities_bot:
  - name: "Constrict"
    desc: "`pf2:1` @Damage[(2d6+7)[bludgeoning]], DC 30 [[Fortitude]] save <br>  <br> The monster deals the listed amount of damage to any number of creatures [[Grabbed]] or [[Restrained]] by it. Each of those creatures can attempt a basic Fortitude save with the listed DC."
  - name: "Glorious Visage"
    desc: "`pf2:1` The asura sanctifies themselves as either holy or unholy, gaining the trait corresponding to their choice and losing the opposing trait; their strikes, spells, and abilities also gain the trait corresponding to their choice. The asura also gains weakness 10 to the opposing sanctification and loses any weakness to its chosen sanctification. The choice is permanent until the asura uses this ability to change their sanctification."
  - name: "Slither"
    desc: "`pf2:1` The garadasura Strides or Swims up to half its Speed, pulling any creatures it has [[Grabbed]] with it."
  - name: "Swallow Whole"
    desc: "`pf2:1` Large, @Damage[(2d10+9)[bludgeoning]], Rupture 30 <br>  <br> The monster attempts to swallow a creature of the listed size or smaller that it has grabbed or restrained in its jaws or mouth. If a swallowed creature is of the maximum size listed, the monster can't use Swallow Whole again. If the creature is smaller than the maximum, the monster can usually swallow more creatures; the GM determines the maximum. The monster attempts an [[Athletics]] check opposed by the grabbed creature's Reflex DC. If it succeeds, it swallows the creature. The monster's mouth or jaws no longer grab a creature it has swallowed, so the monster is free to use them to Strike or Grab once again. The monster can't attack creatures it has swallowed. <br>  <br> A swallowed creature is [[Grabbed]], is [[Slowed]] 1, and has to hold its breath or start suffocating. The swallowed creature takes the listed amount of damage when first swallowed and at the end of each of its turns while it's swallowed. If the victim [[Escapes]] this ability's grabbed condition, it exits through the monster's mouth. This frees any other creature grabbed in the monster's mouth or jaws. A swallowed creature can attack the monster that has swallowed it, but only with unarmed attacks or with weapons of light Bulk or less. The swallowing creature is [[Off-Guard]] against the attack. If the monster takes piercing or slashing damage equaling or exceeding the listed Rupture value from a single attack or spell, the swallowed creature cuts itself free. A creature that gets free by either Escaping or cutting itself free can immediately breathe and exits the swallowing monster's space. <br>  <br> > [!danger] Effect: Engulf and Swallow Whole <br>  <br> If the monster dies, a swallowed creature can be freed by creatures adjacent to the corpse if they spend a combined total of 3 actions cutting the monster open with a weapon or unarmed attack that deals piercing or slashing damage."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Garadasuras are massive ophidian spirits who hold to duties of guardianship and butchery. Many are former naga who have given up on their role of stewards of reality and instead turned their efforts to reversing the act of creation. Garadasuras often continue the duties they had as naga but can also turn destructive, rampaging with the force of an entire poisonous legion.

```statblock
creature: "Garadasura"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
