---
type: creature
group: ["Animal", "Dinosaur"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Allosaurus"
level: "7"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Animal"
trait_02: "Dinosaur"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+15; [[Low-Light Vision]], [[Scent]] (imprecise) 60 feet"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +12, Athletics +17"
abilityMods: ["+6", "+3", "+4", "+0", "+2", "+1"]
abilities_top: []
armorclass:
  - name: AC
    desc: "24; **Fort** +18, **Ref** +15, **Will** +12"
health:
  - name: HP
    desc: "120"
abilities_mid:
  - name: "Serrated Teeth"
    desc: "`pf2:r` **Trigger** A creature [[Grabbed]] or [[Restrained]] by the allosaurus's jaws succeeds at an [[Escape]] check <br>  <br> **Effect** As the enemy wriggles away, the allosaurus clamps down with its jagged teeth, dealing 2d6 slashing damage."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +18 (`pf2:1`) (reach 10 ft.), **Damage** 2d10+9 piercing plus [[Grab]]"
  - name: "Melee strike"
    desc: "Claw +18 (`pf2:1`) (agile), **Damage** 2d8+9 slashing"
  - name: "Melee strike"
    desc: "Tail +18 (`pf2:1`) (reach 15 ft.), **Damage** 2d6+9 bludgeoning plus [[Knockdown]]"
spellcasting: []
abilities_bot:
  - name: "Swallow Whole"
    desc: "`pf2:1` Large, @Damage[(2d6+3)[bludgeoning]], Rupture 15 <br>  <br> The monster attempts to swallow a creature of the listed size or smaller that it has grabbed or restrained in its jaws or mouth. If a swallowed creature is of the maximum size listed, the monster can't use Swallow Whole again. If the creature is smaller than the maximum, the monster can usually swallow more creatures; the GM determines the maximum. The monster attempts an [[Athletics]] check opposed by the grabbed creature's Reflex DC. If it succeeds, it swallows the creature. The monster's mouth or jaws no longer grab a creature it has swallowed, so the monster is free to use them to Strike or Grab once again. The monster can't attack creatures it has swallowed. <br>  <br> A swallowed creature is [[Grabbed]], is [[Slowed]] 1, and has to hold its breath or start suffocating. The swallowed creature takes the listed amount of damage when first swallowed and at the end of each of its turns while it's swallowed. If the victim [[Escapes]] this ability's grabbed condition, it exits through the monster's mouth. This frees any other creature grabbed in the monster's mouth or jaws. A swallowed creature can attack the monster that has swallowed it, but only with unarmed attacks or with weapons of light Bulk or less. The swallowing creature is [[Off-Guard]] against the attack. If the monster takes piercing or slashing damage equaling or exceeding the listed Rupture value from a single attack or spell, the swallowed creature cuts itself free. A creature that gets free by either Escaping or cutting itself free can immediately breathe and exits the swallowing monster's space. <br>  <br> > [!danger] Effect: Engulf and Swallow Whole <br>  <br> If the monster dies, a swallowed creature can be freed by creatures adjacent to the corpse if they spend a combined total of 3 actions cutting the monster open with a weapon or unarmed attack that deals piercing or slashing damage."
  - name: "Unexpected Ambush"
    desc: "`pf2:2` **Requirements** The allosaurus is [[Hidden]] or [[Undetected]] to at least one creature within 40 feet <br>  <br> **Effect** The allosaurus dashes forward, knocking its unsuspecting prey to the ground. The allosaurus Strides up to its Speed toward the required creature to an unoccupied space within reach of its tail Strike. The allosaurus makes a tail Strike against the enemy. If the Strike hits, the allosaurus automatically succeeds at a free action to Knockdown the target."
  - name: "Knockdown"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Knockdown in its damage entry <br>  <br> **Effect** The monster attempts to `act trip` the creature. This attempt neither applies nor counts toward the monster's multiple attack penalty."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

The allosaurus is a huge bipedal dinosaur built for hunting larger prey. Their legs are long and powerful, and their specially hinged jaw allows their mouth to open wide enough to attack creatures who tower over them and to gulp down smaller creatures with frightening ease. Their short arms are tipped in razor-sharp claws, and their thick tails can provide a powerful sweeping defense in a pinch. Occasionally, allosauruses live and hunt in small groups, working together to take down especially large prey. However, they prefer staying in their own territory, reigning over their prey within. Some of their known prey include the brontosaurus, stegosaurus, or whole livestock if an allosaurus strays too close to unprotected farmlands.

```statblock
creature: "Allosaurus"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
