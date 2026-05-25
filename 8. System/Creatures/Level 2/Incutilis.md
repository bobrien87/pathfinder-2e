---
type: creature
group: ["Aberration", "Amphibious"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Incutilis"
level: "2"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Tiny"
trait_01: "Aberration"
trait_02: "Amphibious"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+7; [[Darkvision]]"
languages: "Aklo, Thalassic (Telepathy 30 feet)"
skills:
  - name: Skills
    desc: "Athletics +8, Deception +5, Stealth +9"
abilityMods: ["+4", "+3", "+1", "+1", "+3", "-1"]
abilities_top:
  - name: "Telepathy 30 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
armorclass:
  - name: AC
    desc: "17; **Fort** +7, **Ref** +7, **Will** +9"
health:
  - name: HP
    desc: "21"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Tentacle +8 (`pf2:1`) (unarmed), **Damage** 1d4+4 bludgeoning plus [[Grab]]"
spellcasting: []
abilities_bot:
  - name: "Abandon Puppet"
    desc: "`pf2:1` **Requirements** The incutilis is attached to a puppet <br>  <br> **Effect** The incutilis abandons its puppet, detaching and separating from its nervous system. If the puppet is still alive, it's [[Unconscious]] and temporarily immune to that incutilis's Puppetmaster ability for 24 hours."
  - name: "Puppetmaster"
    desc: "`pf2:3` An incutilis drives tendrils into a Small or Medium living creature that's [[Unconscious]] or [[Restrained]] by the incutilis. They attach and inject the unfortunate host with enzymes to take over control of the creature's nervous system, turning the host into a puppet controlled by the incutilis. <br>  <br> The puppet becomes controlled by the incutilis, and gains dying 2. This doesn't change the puppet's HP, and the puppet can have this dying condition even if it has more than 0 HP. If the puppet dies, its body remains under the control of the incutilis until it's destroyed or the incutilis Abandons the Puppet. <br>  <br> If the puppet recovers from the dying condition, the incutilis immediately Abandons the Puppet. While controlling a puppet, the incutilis is attached to the puppet's head (or elsewhere, if its brain is in an unconventional location) and moves along with it. The puppet uses its own AC, Hit Points, Fortitude and Reflex saves, and physical Strikes, but it uses the incutilis's Will save. The puppet can perform only basic actions and untrained uses of the Athletics and Stealth skills while controlled. <br>  <br> Any attack that deals damage to the puppet also deals 1 mental damage to the incutilis. Area effects are applied to both the incutilis and puppet. The incutilis always has lesser cover while in control of a puppet. <br>  <br> > [!danger] Effect: Cover"
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Incutilises are intelligent, nautilus-like sea creatures that attack their victims' brains to take over their bodies, creating puppets to use for labor, combat, or their own malevolent amusement.

An adult incutilis is slightly smaller than an adult human head, and their shell bears a pattern of crimson streaks that resemble the ridges and furrows of a brain. Incutilises hatch within the depths of the sea, where they start off consuming bottom-dwelling crustaceans and sometimes even whales or sharks. As they grow into adults, incutilises instinctively crave the complex tissues of other creatures' brains—the more complex, the better—preferring to target humanoids and animals.

Eventually, an incutilis will make an excursion onto land specifically to find a puppet to control. Using their tentacles to crawl up onto shore or climb aboard a ship, they then drive their tendrils directly into the brain of a helpless living (or very recently dead) land creature. An incutilis takes control of their new host through this neurological connection. This host—now called a puppet—rarely survives the experience.

After an incutilis has taken full control, they can usually ride their puppet for as long as they wish. Often, they use the puppet to seek out other potential prey, battling other creatures until the wear and tear from repeated conflict renders their current body useless.

```statblock
creature: "Incutilis"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
