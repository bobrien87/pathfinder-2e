---
type: creature
group: ["Amphibious", "Dragon"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Coral Dragon (Ancient, Spellcaster)"
level: "17"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Gargantuan"
trait_01: "Amphibious"
trait_02: "Dragon"
trait_03: "Primal"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+32; [[Darkvision]], [[Wavesense]] (imprecise) 60 feet"
languages: "Common, Draconic, Thalassic"
skills:
  - name: Skills
    desc: "Acrobatics +28, Athletics +30, Diplomacy +34, Intimidation +34, Nature +30, Society +26, Stealth +30, Survival +31"
abilityMods: ["+9", "+5", "+6", "+5", "+5", "+6"]
abilities_top: []
armorclass:
  - name: AC
    desc: "39; **Fort** +32, **Ref** +27, **Will** +28"
health:
  - name: HP
    desc: "315; **Immunities** dazzled, paralyzed, sleep"
abilities_mid:
  - name: "+2 Status to All Saves vs. Primal"
    desc: ""
  - name: "Biomineralize"
    desc: "`pf2:r` **Trigger** The dragon is critically hit by a melee weapon without reach or an unarmed attack that deals slashing or piercing damage <br>  <br> **Effect** A gout of blood spurts from the dragon's wound and instantaneously calcifies into a jagged branch of sharpened coral. The coral branch impales the triggering creature, dealing 8d6 piercing damage (DC 38 [[Reflex]] save). The triggering creature also takes 1d4 persistent,bleed damage on a critical failure. Regardless of the outcome, the coral then crumbles to dust."
  - name: "Kaleidoscopic Display"
    desc: "90 feet. The coral formations covering the dragon's body glow and shimmer with vivid colors, overwhelming the senses and forcing any creature entering or beginning their turn in the aura to attempt a DC 36 [[Fortitude]] save. Regardless of the outcome, the creature is temporarily immune to the dragon's kaleidoscopic display for 1 minute. <br> - **Critical Success** The creature is unaffected. <br> - **Success** The creature is [[Dazzled]] for 1 round. <br> - **Failure** The creature is [[Blinded]] for 1 round. <br> - **Critical Failure** The creature is blinded for 1 round and dazzled for 1 minute."
  - name: "Reef Bond"
    desc: "Every coral dragon is mystically bound to a single living coral reef. If the dragon moves more than 3 miles from their reef, they become [[Sickened]] 1 and unable to recover, with the sickened value increasing by 1 every 6 hours unless they succeed at a DC 40 [[Fortitude]] save. After 24 hours, the dragon becomes [[Drained]] 1; its drained value increases by 1 every 24 hours. <br>  <br> If the dragon's reef suffers significant damage, they immediately become aware of the location where the reef was harmed but not the source or nature of the damage. Should the reef ever be completely destroyed, the dragon is immediately slain."
  - name: "Improved Push"
    desc: "`pf2:0` **Trigger** The monster's last action was a successful Strike that lists Improved Push in its damage entry <br>  <br> **Effect** The monster attempts to `act shove` the creature. This attempt neither applies nor counts toward the monster's multiple attack penalty. If Improved Push lists a distance, change the distance the creature is pushed on a success to that distance."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +34 (`pf2:1`) (magical, reach 20 ft.), **Damage** 3d12+17 piercing plus [[Improved Grab]]"
  - name: "Melee strike"
    desc: "Claw +34 (`pf2:1`) (agile, magical, reach 15 ft.), **Damage** 3d8+17 slashing"
  - name: "Melee strike"
    desc: "Tail +32 (`pf2:1`) (magical, reach 25 ft.), **Damage** 3d10+17 bludgeoning plus [[Improved Knockdown]]"
spellcasting:
  - name: "Primal Prepared Spells"
    desc: "DC 38, attack +30<br>**8th** (3 slots) [[Crashing Wave]], [[Desiccate]], [[Moment of Renewal]]<br>**7th** (3 slots) [[Hydraulic Torrent]], [[Regenerate]], [[Unfettered Pack]]<br>**6th** (3 slots) [[Chameleon Coat]], [[Petrify]], [[Slow]]<br>**5th** (3 slots) [[Control Water]], [[Crashing Wave]], [[Mariner's Curse]]<br>**4th** (3 slots) [[Hydraulic Torrent]], [[Vapor Form]], [[Mirage]]<br>**3rd** (3 slots) [[Aqueous Orb]], [[Crashing Wave]], [[Slow]]<br>**2nd** (3 slots) [[Mist]], [[Water Breathing]], [[Water Walk]]<br>**1st** (3 slots) [[Air Bubble]], [[Create Water]], [[Tailwind]]<br>**Cantrips** [[Detect Magic]], [[Know the Way]], [[Prestidigitation]], [[Spout]], [[Stabilize]]"
abilities_bot:
  - name: "Hydraulic Breath"
    desc: "`pf2:2` The dragon exhales a pressurized jet of water that deals @Damage[18d6[bludgeoning]|options:area-damage] damage in an @Template[type:line|distance:120] (DC 38 [[Reflex]] save). Creatures that critically fail their Reflex save against the Hydraulic Breath are pushed back 10 feet and knocked [[Prone]]. The dragon can't use Hydraulic Breath again for 1d4 rounds."
  - name: "Reef Armor"
    desc: "`pf2:2` **Frequency** once per day <br>  <br> **Effect** The dragon encases themself in an shell of protective coral, gaining 50 temporary Hit Points and resistance 10 to piercing and slashing damage until the temporary Hit Points are depleted. The effect lasts for 1 minute, until destroyed, or until the dragon Dismisses the effect."
  - name: "Reef Meld"
    desc: "`pf2:3` **Frequency** once per day <br>  <br> **Requirements** The coral dragon is in physical contact with their bound reef <br>  <br> **Effect** The dragon physically merges with the reef and vanishes, along with up to eight willing creatures, into an extradimensional space where it can neither affect nor be affected by the outside world. The effect lasts indefinitely or until the dragon Dismisses it. Once merged, the dragon can spend 1 minute traveling to and emerging from any point on its reef up to 10 mile away."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Coral dragons are the primal guardians of the vast living coral reefs found in oceans across Golarion. Even by draconic standards, coral dragons stand out for their arrogance and vanity, boasting inordinate pride in the vibrant hues of their own coral-encrusted scales and the dazzling splendor of the reefs they protect. Coral dragons like to decorate their reefs, which they view as lairs, with objects of beauty, dotted with the occasional bit of valuables like coins. Those who seek the favor of a coral dragon often find the creature easily swayed by flattery, particularly when paired with shiny or brightly colored gifts that complement the scintillating beauty of the dragon and their underwater domain.

```statblock
creature: "Coral Dragon (Ancient, Spellcaster)"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
