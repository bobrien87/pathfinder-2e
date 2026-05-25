---
type: creature
group: ["Fungus", "Plant"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Praskith"
level: "7"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Fungus"
trait_02: "Plant"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+15; [[Low-Light Vision]]"
languages: "Fey (Can't speak any language)"
skills:
  - name: Skills
    desc: "Athletics +15, Stealth +14"
abilityMods: ["+7", "+2", "+5", "-2", "+3", "+0"]
abilities_top:
  - name: "Praskith Venom"
    desc: "**Saving Throw** DC 21 [[Fortitude]] save <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** [[Clumsy]] 2 (1 round) <br>  <br> **Stage 2** clumsy 2 and [[Slowed]] 2 (1 round) <br>  <br> **Stage 3** [[Paralyzed]] (1 round)"
armorclass:
  - name: AC
    desc: "25; **Fort** +17, **Ref** +12, **Will** +13"
health:
  - name: HP
    desc: "120; **Immunities** acid; **Weaknesses** fire 5; **Resistances** piercing 5, slashing 5"
abilities_mid:
  - name: "Reactive Strike (Vine Only)"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Mouth +18 (`pf2:1`) (reach 10 ft.), **Damage** 2d10+11 piercing plus [[Grab]]"
  - name: "Melee strike"
    desc: "Vine +18 (`pf2:1`) (agile, reach 15 ft.), **Damage** 2d6+11 bludgeoning plus [[Grab]]"
spellcasting: []
abilities_bot:
  - name: "Rampant Growth"
    desc: "`pf2:1` **Requirements** A creature the praskith has Swallowed Whole has taken damage since the end of the praskith's last turn, and the praskith hasn't used any other actions this turn <br>  <br> **Effect** The praskith regains 3d8 Hit Points and recovers from the [[Fatigued]] and slowed conditions. It reduces any enfeebled value it has by 2."
  - name: "Swallow Whole"
    desc: "`pf2:1` Large, @Damage[(2d10+7)[acid]] damage plus praskith venom, Rupture 14 <br>  <br> The monster attempts to swallow a creature of the listed size or smaller that it has grabbed or restrained in its jaws or mouth. If a swallowed creature is of the maximum size listed, the monster can't use Swallow Whole again. If the creature is smaller than the maximum, the monster can usually swallow more creatures; the GM determines the maximum. The monster attempts an [[Athletics]] check opposed by the grabbed creature's Reflex DC. If it succeeds, it swallows the creature. The monster's mouth or jaws no longer grab a creature it has swallowed, so the monster is free to use them to Strike or Grab once again. The monster can't attack creatures it has swallowed. <br>  <br> A swallowed creature is [[Grabbed]], is [[Slowed]] 1, and has to hold its breath or start suffocating. The swallowed creature takes the listed amount of damage when first swallowed and at the end of each of its turns while it's swallowed. If the victim [[Escapes]] this ability's grabbed condition, it exits through the monster's mouth. This frees any other creature grabbed in the monster's mouth or jaws. A swallowed creature can attack the monster that has swallowed it, but only with unarmed attacks or with weapons of light Bulk or less. The swallowing creature is [[Off-Guard]] against the attack. If the monster takes piercing or slashing damage equaling or exceeding the listed Rupture value from a single attack or spell, the swallowed creature cuts itself free. A creature that gets free by either Escaping or cutting itself free can immediately breathe and exits the swallowing monster's space. <br>  <br> > [!danger] Effect: Engulf and Swallow Whole <br>  <br> If the monster dies, a swallowed creature can be freed by creatures adjacent to the corpse if they spend a combined total of 3 actions cutting the monster open with a weapon or unarmed attack that deals piercing or slashing damage."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

These strange amalgams of plant and fungus with animal tendencies form where the natural world is corrupted by foul magic or frayed planar boundaries. Praskiths are instinctive ambush predators who seek out lightly traveled forest paths and lie in wait in the undergrowth. A praskith swallows prey as quickly as possible and lets its paralytic digestive juices finish the meal, swiftly restoring itself with the nourishment provided by the trapped creature. When collected, neutralized, and refined, the digestive fluids of a praskith form a lacquer that retains some of the creature's acid resistance.

A praskith comes into being with a rudimentary understanding of the Fey language, but in some cases it might manifest knowing a different tongue, such as Aklo, Draconic, or even Necril. Regardless, praskiths have little patience for chattering with potential meals, though some determined fey and primal spellcasters have been known to form alliances or even closer bonds with praskiths. Befriending a praskith requires great patience and plentiful food—and gifts of food must be alive when handed over.

When finished feeding, a praskith slips into a quiescent state for a full day, one of the few times it's safe to approach. Upon rousing, it seeks the deep forest to regurgitate the less digestible portions of its meal. These remains can contain valuables that survived digestion and indicate that a praskith's hunting grounds lie nearby.

Praskiths dwell in deep woods and jungles. Well-fed praskiths develop fruiting bodies that cast forth millions of spores. Spores that happen to alight on carrion grow into new praskiths.

```statblock
creature: "Praskith"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
